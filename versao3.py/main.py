from pessoa_fisica import PessoaFisica
from conta_corrente import ContaCorrente
from transacoes import *

def menu():
    exibir = """
        Escolha uma operação

        [1] Depositar
        [2] Sacar
        [3] Exibir Extrato
        [4] Cadastrar Cliente
        [5] Cadastrar Conta Corrente
        [6] Listar Clientes
        [7] Listar Contas
        [0] Sair

        => """

    opcao = int(input(exibir))
    return opcao

def filtrar_clientes(cpf, lista_clientes):
    cliente = [usuario for usuario in lista_clientes if cpf == usuario.cpf] 
    return cliente[0] if cliente else None

def filtrar_contas(lista_contas, numero_conta):
    contas = [conta for conta in lista_contas if numero_conta == conta.numero_conta] 
    return contas[0] if contas else None

def procurar_conta(lista_clientes):
    print("\n=================================================")
    cpf = str(input("Digite o CPF do titular da conta: "))

    cliente = filtrar_clientes(cpf, lista_clientes)  

    if cliente:
        numero_conta = str(input("Digite o número da conta: "))
        conta = filtrar_contas(cliente.contas, numero_conta)

        if conta:
            return conta
        else:
            print("Conta não encontrada, por favor, verifique o número digitado.")
        
    else:
        print("O CPF informado não consta na lista de clientes, por favor, primeiro realize o cadastro do cliente.")
    
    return None

def cadastrar_cliente(lista_clientes):
    cpf = str(input("Digite o CPF (somente números): "))

    if (filtrar_clientes(cpf, lista_clientes)):
        print("O CPF digitado já consta como usuário.")
    else:
        print("\n======================================================Novo Cadastro======================================================")
        nome = str(input("Nome completo: "))
        nascimento = str(input("Data de nascimento[00/00/0000]: "))
        endereco = str(input("Digite o endereço no seguinte formato: rua,numero - bairro - cidade/sigla do estado: "))

        novo_cliente = PessoaFisica(endereco, cpf, nome, nascimento)
        lista_clientes.append(novo_cliente)

        print("Cliente cadastrado!")

def cadastrar_conta_corrente(lista_clientes):
    print("\n=================================================")
    print("NOVA CONTA CORRENTE".center(49))
    cpf = str(input("Por favor, digite o CPF do usuário: "))

    cliente = filtrar_clientes(cpf, lista_clientes)  

    if cliente:
        numero_conta = str(input("Digite o número da conta: "))
        nova_conta_corrente = ContaCorrente(cliente, numero_conta)
        cliente.adicionar_conta(nova_conta_corrente)
        print("Conta cadastrada com sucesso!")
    else:
        print("O CPF informado não consta na lista de clientes, por favor, primeiro realize o cadastro do cliente.")

def listar_clientes(lista_clientes):
    print("=======================================================")
    if len(lista_clientes) != 0:
        for cliente in lista_clientes:
            print(cliente)
    else:
        print("Nenhum cliente cadastrado.")
    print("=======================================================")

def listar_contas(lista_clientes):
    nao_tem_conta_cadastrada = True

    print("=======================================================")
    if len(lista_clientes) != 0:
        for cliente in lista_clientes:
            for conta in cliente.contas:
                if conta:
                    print(conta)
                    nao_tem_conta_cadastrada = False

        if nao_tem_conta_cadastrada:
            print("Nenhuma conta cadastrada.")
    else:
        print("Nenhuma conta cadastrada.")
    print("=======================================================")

def main():
    lista_clientes = []

    while True:
        opcao = menu()
        
        if opcao == 1:
            conta = procurar_conta(lista_clientes)
            if conta:
                valor = float(input("Digite o valor para depósito: "))
                deposito = Deposito(valor)
                deposito.registrar(conta)
            else:
                print("Não foi possível realizar a operação.")

        elif opcao == 2:
            conta = procurar_conta(lista_clientes)
            if conta:
                valor = float(input("Digite o valor para saque: "))
                saque = Saque(valor)
                saque.registrar(conta)
            else:
                print("Não foi possível realizar a operação.")

        elif opcao == 3:
            conta = procurar_conta(lista_clientes)
            if conta:
                conta.exibir_extrato()
            else:
                print("Não foi possível exibir o extrato.")
        
        elif opcao == 4:
            cadastrar_cliente(lista_clientes)
            
        elif opcao == 5:
            cadastrar_conta_corrente(lista_clientes)
        
        elif opcao == 6:
            listar_clientes(lista_clientes)
        
        elif opcao == 7:
            listar_contas(lista_clientes)

        elif opcao == 0:
            print("Saindo...")
            break
        
        else:
            print("Opção Inválida! Por favor, selecione novamente a operação desejada.")

main()