menu = """
--------------------------------------------------
    [1]Deposito
    [2]Saque
    [3]Extrato
    [4]Sair
--------------------------------------------------
"""
saldo = 0
limite = 500
numero_saques = 1
extrato = ""
LIMITE_SAQUE = 3

while True:
    opcao = int(input(menu))
    if(opcao == 1):
        deposito = int(input("Valor do deposito: "))
        print(" ")

        if(deposito > 0):
            saldo += deposito
            extrato = extrato + f"""
Deposito no valor de R$ {deposito:.2f}
"""
        else:
            print("Não é possivel utilizar valores negativos, tente novamente!")
    elif(opcao == 2):
        saque = int(input("Valor do saque: "))
        print(" ")

        if(saldo >= saque and saque <= limite and LIMITE_SAQUE >= numero_saques):
            print("Saque realizado com sucesso!")
            extrato = extrato + f"""
Saque no valor de R$ {saque:.2f}
"""
            numero_saques += 1
            saldo -= saque
        elif(saldo < saque):
            print("Saldo insuficiente!")
        elif(saque >= 500):
            print("Valor acima do limite!")
        elif(LIMITE_SAQUE <= numero_saques):
            print("Você atingiu seu limite de saques diários!")
        else:
            print("Opção insiponivel, tente novamente")

    elif(opcao == 3):
        if(extrato == ""):
            print("Não foram realizadas movimentações na conta")
        else:    
            print("Extrato".center(50,"-"))
            
            print(extrato)
            print(f"Saldo R$ {saldo:.2f}")
            print("-"*50)

    elif(opcao == 4):
        print(f"\nObrigado pela preferência, até logo!\n")
        break

    else:
        print(f"\nOpção não disponível, digite as opções mostradas no menu.")
        