from datetime import datetime

class Historico():

    def __init__(self):
        self.__transacoes = list()
    
    @property
    def transacoes(self):
        return self.__transacoes

    def adicionar_transacao(self, transacao):
        self.__transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%s")
        })