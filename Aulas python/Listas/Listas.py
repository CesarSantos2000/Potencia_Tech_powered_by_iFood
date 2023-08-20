lista = []

#.append() - adiciona itens a lista
lista.append(1)
lista.append("Python")
lista.append([40, 50, "Cesar"])

print(lista)

#.clear() - Apaga todos os itens da lista
lista.clear()

print(lista)

#.copy() - Atribui a uma lista os atributos de uma lista existente, mas seus atributos não mudam caso a lista original mude na execução
lista = [1, 4, "Cesar", "Maria"]
l2 = lista.copy()

print(lista)
print(l2)
print(id(lista), id(l2))

lista.append(28)

print(lista)
print(l2)

#.count() - Retorna quantos vezes um item selecionado aparece na lista
print(lista.count("Maria"))

#.extend() - Concatena duas listas

lista.extend(l2)
print(lista) 

#.index() - Informa o primeiro indice do item selecionado
print(lista.index("Maria"))

#.index() - Remove o último elemento da lista ou o elemento na posição escolhida
lista.pop(0)
print(lista)

#.pop() - Remove um item da sua lista, mas o item é indicado diretamente e não pelo indice
lista.remove(4)
print(lista)

#.reverse() - Faz o espelhamento da lista
lista.reverse()
print(lista)

#.sort() - Faz uma ordenação de acordo com os parâmetros passados peli usúario
lista.clear()
lista = ["Bola", "Carro", "Cesar", "Maria"]
lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)

lista.sort(key=lambda x: len(x))
print(lista)

lista.sort(key=lambda x: len(x), reverse=True)
print(lista)