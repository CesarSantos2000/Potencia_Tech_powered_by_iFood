opcao = -1
saldo = 15000

while opcao!= 0:
    opcao = int(input("[1]saque, [2]Extrato, [0]Para sair: "))
    if(opcao == 1):
        saque = int(input("Valor do saque: "))
        if(saldo >= saque):
            print("Saque realizado com sucesso!")
        else:
            print("Saldo indisponível!")
    elif(opcao == 2):
        print("Imprimindo extrato!")
    else:
        print("Opção inválida, retornando para o primeiro menu!")