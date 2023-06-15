from PySide6.QtWidgets import QWidget
from interfaceAG import Ui_Form
from ag import AG 


class Widget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ag = AG()
        self.btnResult.clicked.connect(self.clickedButtonResult)
        self.btnResultDefault.clicked.connect(self.clickedButtonResultDefault)



    def clickedButtonResult(self):
        tam = int(self.TAM.text())
        tamanho_populacao = int(self.TP.text() )
        numero_geracoes = int(self.NG.text())
        taxa_cruzamento = float(self.TC.text())
        taxa_mutacao = float(self.TM.text())
        intervalo_geracao = float(self.IG.text())
        
        mat = self.ag.gerar_problema(tam,10,50)

        pop = self.ag.rotina_ag(mat,tam,
                 tamanho_populacao,
                 numero_geracoes,
                 taxa_cruzamento,
                 taxa_mutacao,
                 intervalo_geracao
                 )

        string = "Solução final \t"+str(pop)

        self.Result.setPlainText(string)

    def clickedButtonResultDefault(self):

        tam  =  [10,30,50,100]         # TAMANHO DO CROMOSSOMO
        tamanho_populacao =  [20,50,100,300,500]   
        numero_geracoes =  [50,100,200,500]       
        taxa_cruzamento =  [0.4,0.6,0.8,0.9]
        taxa_mutacao =  [0,0.05,0.1,0.2,0.5]
        intervalo_geracao =  [0,0.1,0.2,0.5]
        populacao = ""
        
        for problem in tam:
            str2 = "Dados" + str(problem) + ".txt"
            f = open(str2,"w")
            out = "tp,tc,tm,ig,ng,custo"
            mat = self.ag.gerar_problema(problem,5,50)
            for tp in tamanho_populacao:
                for tc in taxa_cruzamento:
                    for tm in taxa_mutacao:
                        for ng in numero_geracoes:
                            for ig in intervalo_geracao:
                                print(problem,tp,tc,tm,ng,ig)
                                populacao = self.ag.rotina_ag(mat,problem,tp,ng,tc,tm,ig)
                                out = str(tp) + "," + str(ng) + "," + str(tc) + "," +  str(tm) + "," +  str(ig) + "," + str(populacao)
                                f.write(out)
            f.close()
