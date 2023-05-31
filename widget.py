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
        tamanho_populacao = int(self.TP.text())
        numero_geracoes = int(self.NG.text())
        taxa_cruzamento = int(self.TC.text())
        taxa_mutacao = int(self.TM.text())
        intervalo_geracao = int(self.IG.text())
        
        mat = self.ag.gerar_problema(tam,5,20)

        sol = self.ag.rotina_ag(mat,tam,
                 tamanho_populacao,
                 numero_geracoes,
                 taxa_cruzamento,
                 taxa_mutacao,
                 intervalo_geracao
                 )

        string = str(sol)
        self.Result.setPlainText(string)

    def clickedButtonResultDefault(self):
        tam = int(self.TAM.text())
        mat = self.ag.gerar_problema(tam,5,20)

        sol = self.ag.rotina_ag(mat,
                                tam,
                 15,
                 50,
                 0.8,
                 0.1,
                 0.2
                 )

        string = str(sol)
        self.Result.setPlainText(string)