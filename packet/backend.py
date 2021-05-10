from packet.Class_doc import Doc
from packet.Class_midia import Midia
doc = Doc()
midia = Midia()

class Backend:
    def __init__(self):
        pass
    def Programa(self):
        midia.banner()
        doc.pesquisa_IP_cria_manipula_csv()
        midia.doc_finalizado()


