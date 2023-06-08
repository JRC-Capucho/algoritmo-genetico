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
            print(desc)

            # ajusta descentendes = restricao do problema
            desc = self.ajusta_restricao(tam,desc,len(desc),corte)
            print('new desc \t', desc)

        return populacao, fit, corte, desc

    """"
            # mutacao
            desc = self.mutacao(tam,desc,tamanho_populacao,taxa_mutacao)

            # ordena pop atual
            if ig != 0:
                populacao, fit = sort(populacao,fit,tamanho_populacao)
            
            # ordem descendente
            desc, fitd_d = sort(desc,fit_d,len(desc))

            # gera nova
            populacao = self.novapop(populacao,desc,fit,fit_d,tamanho_populacao,intervalo_geracao)

            # fit da nova pop
            fit = self.aptidao(tam,tamanho_populacao,populacao,mat)

        pop, fit = sort(populacao,fit,tamanho_populacao)
        return popt[0]
    """



