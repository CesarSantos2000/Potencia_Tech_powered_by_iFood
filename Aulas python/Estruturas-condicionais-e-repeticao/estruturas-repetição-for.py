texto = input("Digite um texto: ")
VOGAIS = "AEIOU"

for i in texto:
    if i.upper() in VOGAIS:
        print(i, end=" ")
print("")

for i in range(0, 51, 5):
    print(i, end=" ")