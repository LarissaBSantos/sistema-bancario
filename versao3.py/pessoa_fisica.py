from cliente import Cliente

class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.__cpf = cpf
        self.__nome = nome
        self.__data_nascimento = data_nascimento
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def data_nascimento(self):
        return self.__data_nascimento

    def __str__(self):
        return f"""
                    Nome:\t\t\t{self.nome}
                    CPF:\t\t\t{self.cpf}
                    Data de Nascimento:\t\t{self.data_nascimento}
                    Endereço:\t\t\t{self.endereco}
                """