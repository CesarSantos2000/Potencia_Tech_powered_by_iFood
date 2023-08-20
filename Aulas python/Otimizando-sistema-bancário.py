def menu():
    menu = """
--------------------------------------------------
    [1]Deposito
    [2]Saque
    [3]Extrato
    [4]Criar usúario
    [5]Criar conta
    [6]Listar contas
    [7]Sair
--------------------------------------------------
"""
    opcao = int(input(menu))
    return opcao

def deposito(valor, saldo, extrato, /):

    if(valor > 0):
        saldo += valor
        extrato = extrato + f"""
Deposito: \tR$ {valor:.2f}
"""
    else:
        return print("Não é possivel utilizar valores negativos, tente novamente!")
    return saldo, extrato

def saque(*,valor, saldo, extrato, limite, numero_saques, limite_saques):

    excedeu_saldo = saldo < valor
    excedeu_limite = valor > limite
    excedeu_saques = limite_saques < numero_saques
 
    if(excedeu_saldo):
        print("Saldo insuficiente!")
    elif(excedeu_limite):
        print("Valor acima do limite!")

    elif(excedeu_saques):
        print("Você atingiu seu limite de saques diários!")

    elif(valor > 0):
        numero_saques += 1
        saldo -= valor
        extrato = extrato + f"""
Saque: \t\tR$ {valor:.2f}
"""
        print("Saque realizado com sucesso!")
    
    else:
        print("Opção insiponivel, tente novamente")
    return saldo, extrato, numero_saques

def func_extrato(saldo, /, *, extrato):
    if(extrato == ""):
        return print("Não foram realizadas movimentações na conta")
    else:    
        return print("Extrato".center(50,"-")), print(extrato), print(f"\nSaldo:\t\tR$ {saldo:.2f}"), print("-"*50)

def criar_usuario(usuarios):
    cpf = input("Digite seu CPF(Somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Opçãop invalída, conta existente!")
    else:
        nome = input("Digite seu nome completo?")
        data_nascimento = input("Digite sua data de nascimento:")
        endereco = input("Digite seu endereco(logradouro, nro - bairro - cidade/sigla estado):")

        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        print("Usúario criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf ]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite seu CPF(Somente números):")
    usuario_filtrado = filtrar_usuario(cpf, usuarios)

    if usuario_filtrado:
        print("Conta criada com sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario_filtrado}

def listar_contas(contas):
    for conta in contas:
        lista_de_contas = f"""
Agência = {conta['agencia']}
C/C = {conta['numero_conta']}
Tirular = {conta['usuario']['nome']}
"""
        print("-"*50)
        print(lista_de_contas)

def main():   
    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    numero_saques = 1
    extrato = ""
    usuarios = []
    contas = []
    

    while True:
        
        opcao = menu()
        if(opcao == 1):
            valor = float(input("Valor do deposito: "))
            print(" ")
            saldo, extrato = deposito(valor, saldo, extrato)

        elif(opcao == 2):
            valor = int(input("Valor do saque: "))
            saldo, extrato, numero_saques = saque(valor=valor, saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUE)
            print(numero_saques)
        elif(opcao == 3):
            func_extrato(saldo, extrato=extrato)
        
        elif(opcao == 4):
            criar_usuario(usuarios)
        
        elif(opcao == 5):
            numero_conta = len(contas)+1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            contas.append(conta)

        elif(opcao == 6):
            listar_contas(contas)

        elif(opcao == 7):
            print(f"\nObrigado pela preferência, até logo!\n")
            break

        else:
            print(f"\nOpção não disponível, digite as opções mostradas no menu.")

main()

