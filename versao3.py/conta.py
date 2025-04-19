from historico import Historico
from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, cliente, numero_conta):
        self.__saldo = 0
        self.__numero_conta = numero_conta
        self.__agencia = "0001"
        self.__cliente = cliente
        self.__historico = Historico()
    
    @classmethod
    def nova_conta(cls, cliente, numero_conta):
        return cls(cliente, numero_conta)
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def numero_conta(self):
        return self.__numero_conta
    
    @property
    def historico(self):
        return self.__historico

    @property
    def agencia(self):
        return self.__agencia
    
    @property
    def cliente(self):
        return self.__cliente
    
    def sacar(self, valor):
        excedeu_saldo = valor > self.saldo

        if excedeu_saldo:
            print("###Operação Falhou! Saldo insuficiente.")
        
        elif valor > 0:
            self.__saldo -= valor
            print("***Saque realizado com sucesso!")
            return True
        
        else:
            print("###Operação Falhou! O valor informado é inválido.")
        
        return False

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print("***Depósito realizado com sucesso!")
            return True
        else:
            print("###Operação Falhou! O valor informado é inválido.")
            return False
    
    def exibir_extrato(self):
        print("\n========================Extrato========================")
        
        if (len(self.historico.transacoes) == 0):
            print("Não foram realizadas movimentações.")
        else:
            for transacao in self.historico.transacoes:
                exibir_transacao = f"""\t{transacao["tipo"]}\n\tValor:\tR$ {transacao["valor"]:.2f}\n\tData:\t{transacao["data"]}\n"""
                print(exibir_transacao)
            print(f"\n\tSaldo:\tR$ {self.saldo:.2f}\n")
            print("========================================================")
    
    @abstractmethod
    def __str__(self):
        pass