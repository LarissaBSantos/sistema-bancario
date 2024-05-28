menu = """
Escolha uma operação

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

LIMITE = 500  
limite_saques = 3
saldo = 0
saque = 0
extrato = ""

while True:
    opcao = int(input(menu))

    if opcao == 1:
        deposito = float(input("Digite o valor: "))
        if deposito > 0:
            saldo += deposito
            extrato = f"""{extrato} Depósito de R$ {deposito:.2f}\n"""
            print("Operação efetuada com sucesso!") 
        else:
            print("Operação falhou! O valor informado é inválido.") 

    elif opcao == 2:
        if limite_saques > 0:
            saque = float(input("Digite o valor: "))
            if saque > 0:
                if saque <= saldo:
                    if saque <= LIMITE:
                        limite_saques -= 1
                        saldo -= saque
                        extrato = f"""{extrato} Saque de R$ {saque:.2f}\n"""
                        print("Operação efetuada com sucesso, por favor, retire seu dinheiro!")    
                    else:
                        print("Operação falhou! O limite máximo de saque é R$ 500.00")
                else:
                    print("Operação falhou! Não será possível sacar o dinheiro por falta de saldo.\n")
            else:
                print("Operação falhou! O valor informado é inválido.")
        else:
            print("Operação falhou! O limite de saque diário atingido.")

    elif opcao == 3:
        print("\n========================Extrato========================")
        print(f"{extrato}\n\n Saldo Atual: R$ {saldo:.2f}")
        print("========================Extrato========================")

    elif opcao == 4:
        print("Saindo...")
        break

    else:
        print("Opção Inválida! Por favor, selecione novamente a operação desejada.")

    
