saldo = 1000
saque = 800
limite = 500
conta_especial = False

"""" Forma de ddificil visualização """

print(saldo >= saque and saque <= limite or conta_especial and saldo >= saque)

""" Melhor forma para a visualização """

print((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque))


""" Tabela para entendimento dos operadores lógicos"""

print(True and True)
print(True and False)
print(True or True)
print(True or False)
print(False and False)