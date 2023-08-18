tipo_conta = int(input("Digite 1 para conta normal ou 2 para conta universitaria:"))


saldo = 2000
cheque_especial = 500
saque = int(input("Digite o valor do saque:"))

if(tipo_conta == 1):
    if(saldo >= saque):
        print("Saque realizado com sucesso!")
    elif(saque <= saldo+cheque_especial):
        print("Saque realizado com sucesso!")
    else:
        print("Saldo indisponível")
elif(tipo_conta == 2):
    if(saldo >= saque):
        print("Saque realizado com sucesso!")
    else:
        print("Saldo indisponível")       
else:
    print("Não foi possível realizar o saque, por favor fale com o banco!")