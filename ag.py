from numpy import zeros
from random import randrange, shuffle

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

    def rotina_ag(self,
                  mat,tam,
                  tamanho_populacao,
                  numero_geracao,
                  taxa_cruzamento,
                  taxa_mutacao,
                  intervalo_geracao):
        populacao = self.populacao_inicial(tam,tamanho_populacao)
        return populacao
    """"
        fit = aptidao(tam,tamanho_populacao,populacao,mat)

        for g in range(numero_geracao):
            corte, desc = crossover(tam,populacao,fit,tamanho_populacao,taxa_cruzamento)

            desc = ajusta_restricao(tam,desc,len(desc))

            desc = mutacao(tam,desc,tamanho_populacao,taxa_mutacao)

            if ig != 0:
                populacao, fit = sort(populacao,fit,tamanho_populacao)
            
            desc, fitd_d = sort(desc,fit_d,len(desc))
            populacao = novapop(populacao,desc,fit,fit_d,tamanho_populacao,intervalo_geracao)
            fit = aptidao(tam,tamanho_populacao,populacao,mat)

        pop, fit = sort(populacao,fit,tamanho_populacao)
        return popt[0]

    """



