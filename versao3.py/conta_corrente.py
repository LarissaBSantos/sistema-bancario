from conta import Conta
from transacoes import *

class ContaCorrente(Conta):

    def __init__(self, cliente, numero_conta, limite_saques = 3, limite = 500):
        super().__init__(cliente, numero_conta)
        self.__limite = limite
        self.__limite_saques = limite_saques

    @property
    def limite(self):
        return self.__limite
    
    @property
    def limite_saques(self):
        return self.__limite_saques
    
    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes
                            if transacao["tipo"] == Saque.__name__])

        if numero_saques >= self.limite_saques:
            print("###Operação falhou! Limite de saque diário excedido.")
            return False
        
        elif valor > self.limite:
            print("###Operação Falhou! O limite máximo de saque é R$ 500.00.")
            return False
        
        else:
            return super().sacar(valor)
    
    def __str__(self):
        return f"""
                Titular:\t{self.cliente.nome}
                Agência:\t{self.agencia}
                C/C:\t\t{self.numero_conta}
                Saldo:\t\tR$ {self.saldo:.2f}
                """