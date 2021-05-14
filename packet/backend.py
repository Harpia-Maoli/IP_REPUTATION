from packet.Class_doc import Doc
from packet.Class_midia import Midia

class Backend:
    def __init__(self, arquivo=""):
        self.arquivo = arquivo
        self.doc = Doc()
        self.midia = Midia()
        self.__Programa()

    def __Programa(self):
        self.midia.banner()
        self.doc.pesquisa_IP_cria_manipula_csv(self.arquivo)
        self.midia.doc_finalizado()


