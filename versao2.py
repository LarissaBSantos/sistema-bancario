import textwrap

# Função que exibe o menu 
def menu():
    exibir = """
    Escolha uma operação

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Cadastrar Cliente
    [5] Cadastrar Conta Corrente
    [6] Listar Contas
    [7] Sair

    => """

    opcao = int(input(exibir))
    return opcao

# Função de depósito
def depositar(saldo_atual, valor, novo_extrato, /,):
    if valor > 0:
        saldo_atual += valor
        novo_extrato = f"""{novo_extrato} Depósito de R$ {valor:.2f}\n"""
        print("Operação efetuada com sucesso!") 
    else:
        print("Operação falhou! O valor informado é inválido.") 
    return saldo_atual, novo_extrato

# Função que verifica se será possível realizar o saque
def vericar_saque(*, saldo_atual, valor_saque, valor_maximo, saques_diarios):
        excedeu_saldo = valor_saque > saldo_atual
        excedeu_valor_limite = valor_saque > valor_maximo
        excedeu_saques =  saques_diarios <= 0

        if excedeu_saldo:
            print("Operação falhou! Não será possível sacar o dinheiro por falta de saldo.\n")

        elif excedeu_valor_limite:
            print("Operação falhou! O limite máximo de saque é R$ 500.00")

        elif excedeu_saques:
            print("Operação falhou! Limite de saque diário excedido.")

        elif(valor_saque <= 0):
            print("Operação falhou! O valor informado é inválido.")

        else:
            return True

# Função de saque
def sacar(*, saldo_atual, valor_saque, novo_extrato, saques_restantes):
    saldo_atual -= valor_saque
    novo_extrato = f"""{novo_extrato} Saque de R$ {valor_saque:.2f}\n"""
    print("Operação efetuada com sucesso, por favor, retire seu dinheiro!")  
    saques_restantes -= 1

    return saldo_atual, novo_extrato, saques_restantes

# Função que exibe o extrato
def mostrar_extrato(saldo, /, *, extrato):
    print("\n========================Extrato========================")
    print(" Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\n Saldo Atual: R$ {saldo:.2f}")
    print("========================================================")

# Função que verifica se o CPF digitado está na lista de clientes
def filtrar_clientes(cpf, lista_clientes):
    cliente = [usuario for usuario in lista_clientes if cpf == usuario["cpf"]] 
    return cliente[0] if cliente else None

# Função que cadastra novo usuário do banco
def cadastrar_cliente(lista_clientes):
    cpf = str(input("Digite o CPF (somente números): "))

    if (filtrar_clientes(cpf, lista_clientes)):
        print("O CPF digitado já consta como usuário.")
    else:
        print("\n======================================================Novo Cadastro======================================================")
        nome = str(input("Nome completo: "))
        nascimento = str(input("Data de nascimento[00/00/0000]: "))
        endereco = str(input("Digite o endereço no seguinte formato: rua,numero - bairro - cidade/sigla do estado: "))
        lista_clientes.append({"cpf": cpf, "nome": nome, "nascimento": nascimento, "endereco": endereco})
        print("Cliente cadastrado!")

# Função que cadastra uma nova conta corrente, essa conta precisa obrigatoriamente está associada a um usuário do banco
def cadastrar_conta(lista_clientes, lista_contas, ultima_conta):
    print("\n=================================================")
    print("NOVA CONTA CORRENTE".center(49))
    cpf = str(input("Por favor, digite o CPF do usuário: "))
    cliente = filtrar_clientes(cpf, lista_clientes)  

    if cliente:
        lista_contas.append({"agencia": "0001", "numero_da_conta": ultima_conta, "nome_titular": cliente["nome"], "cpf": cpf})
        print("Conta cadastrada com sucesso!")
        ultima_conta += 1
    else:
        print("O CPF informado não consta na lista de clientes, por favor, primeiro realize o cadastro do cliente.")

    return ultima_conta

#Função que lista todas as contas
def listar_contas(lista_contas):
    print("=======================================================")
    for conta in lista_contas:
        exibir_contas = f"""
        Titular:\t {conta["nome_titular"]}
        Agência:\t {conta["agencia"]}
        Número da conta: {conta["numero_da_conta"]}\n
        """

        print(textwrap.dedent(exibir_contas))
    print("=======================================================")

def main():
    # Declaração de variáveis
    LIMITE = 500  
    limite_saques = 3
    saldo = 0
    saque = 0
    extrato = ""
    lista_de_clientes = []
    lista_de_contas = []
    ultima_conta = 1

    while True:
        opcao = menu()
        
        if opcao == 1:
            deposito = float(input("Digite o valor: "))
            retorno = depositar(saldo, deposito, extrato)
            saldo = retorno[0]
            extrato = retorno[1]     

        elif opcao == 2:
            saque = float(input("Digite o valor: "))
            saque_valido = False
            saque_valido = vericar_saque(saldo_atual=saldo, valor_saque=saque, valor_maximo=LIMITE, saques_diarios=limite_saques)
            if saque_valido:
                retorno = sacar(saldo_atual=saldo, valor_saque=saque, novo_extrato=extrato, saques_restantes=limite_saques)
                saldo = retorno[0]
                extrato = retorno[1]
                limite_saques = retorno[2]

        elif opcao == 3:
            mostrar_extrato(saldo, extrato=extrato)
        
        elif opcao == 4:
            cadastrar_cliente(lista_de_clientes)
        
        elif opcao == 5:
            ultima_conta = cadastrar_conta(lista_de_clientes, lista_de_contas, ultima_conta)
        
        elif opcao == 6:
            listar_contas(lista_de_contas)

        elif opcao == 7:
            print("Saindo...")
            break

        else:
            print("Opção Inválida! Por favor, selecione novamente a operação desejada.")

main()