MAIOR_IDADE = 18
IDADDE_ESPECIAL = 12

idade = int(input("Digite sua idade: "))

if (idade >= MAIOR_IDADE):
    print("Você pode tirar sua habilitação!")
else:
    print("Você não tem idade suficiente para tirar habilitação!")



if (idade >= MAIOR_IDADE):
    print("Você pode tirar sua habilitação!")
elif(idade >= IDADDE_ESPECIAL):
    print("Você só pode fazer aulas teorícas12!")
else:
    print("Você não tem idade suficiente para tirar habilitação!")
