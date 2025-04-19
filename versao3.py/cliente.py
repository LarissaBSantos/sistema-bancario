from abc import ABC, abstractmethod

class Cliente(ABC):
    def __init__(self, endereco):
        self.__endereco = endereco
        self.__contas = list()
    
    @property
    def endereco(self):
        return self.__endereco
    
    @property
    def contas(self):
        return self.__contas       
    
    @endereco.setter
    def endereco(self, novo_endereco):
        self.__endereco = novo_endereco
    
    def adicionar_conta(self, conta):
        if conta.numero_conta in self.__contas:  # Verifica se a conta esta cadastrada na lista de contas do cliente
            return False
        else:
            self.__contas.append(conta)
            return True
    
    def realizar_transacao(conta, transacao):
        transacao.registrar(conta)
    
    @abstractmethod
    def __str__(self):
        pass