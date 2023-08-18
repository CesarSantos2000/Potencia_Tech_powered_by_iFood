nome = "cesar"
idade = 23
profissao = "Programador"
linguagem = "Python"
avaliacao = 9.7777

# primeiro metrodo, não recomendado com %

print("Me chamo %s. Tenho %d anos de idade. Sou %s e minha linguagem é %s." %(nome, idade, profissao, linguagem))
print("-" * 100)

# Segundo método, utilizando o .format

print("Me chamo {}. Tenho {} anos de idade. Sou {} e minha linguagem é {}." .format(nome, idade, profissao, linguagem))
print("Me chamo {1}. Tenho {0} anos de idade. Sou {3} e minha linguagem é {2}." .format(idade, nome, linguagem, profissao))
print("Me chamo {nome}. Tenho {idade} anos de idade. Sou {profissao} e minha linguagem é {linguagem}." .format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

print("-" * 100)
# Terceiro método e o mais recomendado é formatação com o f-string

print(f"Me chamo {nome}. Tenho {idade} anos de idade. Sou {profissao} e minha linguagem é {linguagem}.")
print(f"Me chamo {nome}. Tenho {idade} anos de idade. E minha avaliação em python é {avaliacao:.2f}.")
