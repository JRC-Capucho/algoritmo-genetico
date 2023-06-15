from copy import deepcopy
from numpy import zeros
from random import randrange, shuffle, uniform
from math import ceil

class AG():
    def gerar_problema(self,tam,min,max):
        mat = zeros((tam,tam), int)
        for i in range(tam):
            for j in range(tam):
                if i != j:
                    mat[i][j] = randrange(min,max)
        return mat

    def cromossomo(self,tam):
        ind = zeros(tam,int)
        for i in range(tam):
            ind[i] = i
        shuffle(ind)

        return ind

    def populacao_inicial(self,tam,tamanho_populacao):
        populacao = zeros((tamanho_populacao,tam),int)

        for i in range(tamanho_populacao):
            populacao[i] = self.cromossomo(tam)

        return populacao

    def custo_caminho(self,p,tam,mat):
        valor = 0
        for i in range(tam-1):
            valor += mat[p[i]-1][p[i+1]-1]
        valor += mat[p[tam-1]-1][p[0]-1]

        return valor

    def aptidao(self,tam,tamanho_populacao,populacao,mat):
        fit = []
        for ind in populacao:
            fit.append(1/self.custo_caminho(ind,tam,mat))

        soma = sum(fit)
        fit /= soma

        return fit

    def roleta(self,fit):
        ale = uniform(0,1)
        ind = 0
        soma = fit[ind]
        
        while soma < ale:
            soma += fit[ind]
            ind += 1

        return ind

    def torneio(self,fit,tamanho_populacao):
        i1 = randrange(0,tamanho_populacao)
        i2 = randrange(0,tamanho_populacao)

        if fit[i1] > fit[i2]:
            return i1
        else:
            return i2


    def cruzamento(self,tam,
                   populacao,
                   fit,
                   tamanho_populacao,
                   taxa_cruzamento):

        quantidade_cruzamento = ceil(taxa_cruzamento * tamanho_populacao)
        
        corte = randrange(1,tam)

        desc = []

        for i in range(quantidade_cruzamento):
            pai1 = self.roleta(fit)
            pai2 = self.roleta(fit)

            # primerio descendente
            aux = []
            for j in range(corte):
                aux.append(populacao[pai1][j])
            for j in range(corte,tam):
                aux.append(populacao[pai2][j])
            desc.append(aux)

            # segundo descendente
            aux = []
            for j in range(corte):
                aux.append(populacao[pai2][j])
            for j in range(corte,tam):
                aux.append(populacao[pai1][j])
            desc.append(aux)

        return corte, desc



    def ajusta_restricao(self,
                         tam,
                         desc,
                         quantidade_descendente,
                         corte):

        for i in range(len(desc)):
            alfabeto = list(range(0,tam))
            for j in range(corte):
                alfabeto.remove(desc[i][j])
                shuffle(alfabeto)
                
            j = corte

            while(len(alfabeto)>0):
                if(desc[i].count(alfabeto[0])==0):
                    if(desc[i].count(desc[i][j])>1):
                        desc[i][j] = alfabeto[0]
                        del alfabeto[0]
                        j += 1
                    else:
                        j +=1
                else:
                    del alfabeto[0]
        return desc

    def mutacao(self,
                tam,
                descendente,
                tamanho_populacao,
                taxa_mutacao):

        quantidade_mutacao = ceil(tamanho_populacao * taxa_mutacao)
        quantidade_descendente = len(descendente)

        for i in range(quantidade_mutacao):
            desc = randrange(0,quantidade_mutacao)
            aux = deepcopy(descendente[desc])

            p1 = randrange(0,tam)
            p2 = randrange(0,tam)

            x = aux[p1]
            aux[p1] = aux[p2]
            aux[p2] = x

            descendente.append(aux)

        return descendente

    def sort(self,populacao,fit,tamanho_populacao):
        for i in range(tamanho_populacao - 1):
            for j in range(i+1,tamanho_populacao):
                if fit[i] < fit[j]:
                    aux_fit = deepcopy(fit[i])
                    fit[i]  = deepcopy(fit[j])
                    fit[j]  = deepcopy(aux_fit)

                    aux_populacao = deepcopy(populacao[i])
                    populacao[i]  = deepcopy(populacao[j])
                    populacao[j]  = deepcopy(aux_populacao)
        return populacao, fit

    def nova_populacao(self,
                       populacao,
                       descendente,
                       tamanho_populacao,
                       intervalo_geracao):
        elite = ceil(tamanho_populacao * intervalo_geracao)
        j = 0
        for i in range(elite,tamanho_populacao):
            populacao[i] = deepcopy(descendente[j])
            j += 1
            if j == len(descendente):
                break

        return populacao


    def rotina_ag(self,
                  mat,tam,
                  tamanho_populacao,
                  numero_geracao,
                  taxa_cruzamento,
                  taxa_mutacao,
                  intervalo_geracao):

        # ger pop inicial
        populacao = self.populacao_inicial(tam,tamanho_populacao)

        # calcula fit
        fit = self.aptidao(tam,tamanho_populacao,populacao,mat)

        # ciclo
        for g in range(numero_geracao):
            # cruzamento
            corte, desc = self.cruzamento(tam,populacao,fit,tamanho_populacao,taxa_cruzamento)
            # print(desc)

            # ajusta descentendes = restricao do problema
            desc = self.ajusta_restricao(tam,desc,len(desc),corte)
            # print('new desc \t', desc)

            # mutacao
            desc = self.mutacao(tam,desc,tamanho_populacao,taxa_mutacao)

            fit_d = self.aptidao(tam,len(desc),desc,mat)

            # ordena pop atual
            populacao, fit = self.sort(populacao,fit,tamanho_populacao)
            
            # ordem descendente
            desc, fit_d = self.sort(desc,fit_d,len(desc))

            # gera nova
            populacao = self.nova_populacao(
                       populacao,
                       desc,
                       tamanho_populacao,
                       intervalo_geracao)

            # fit da nova pop
            fit = self.aptidao(tam,tamanho_populacao,populacao,mat)

        pop, fit = self.sort(populacao,fit,tamanho_populacao)
        return pop[0]
