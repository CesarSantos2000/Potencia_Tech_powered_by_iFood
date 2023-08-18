opcao = -1

while True:
    opcao = int(input("Digite um número: "))
    if(opcao % 2 == 0):
        print(f"O número {opcao} é par")
        break
    else:
        print(f"O número {opcao} é impar.")