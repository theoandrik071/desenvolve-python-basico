q1 = int(input("Digite a quantidade de elementos da lista 1:"))
lista1 = []
for i in range(q1):
    n1 = int(input(f"Digite os {i+1} elementos da lista 1:"))
    lista1.append(n1)
q2 = int(input("Digite a quantidade de elementos da lista 1:"))
lista2 = []
for i in range(q2):
    n2 = int(input(f"Digite os {i+1} elementos da lista 1:"))
    lista2.append(n2)
lista_intercalada = []
tamanho_max = max(len(lista1), len(lista2))
for i in range(tamanho_max):
    if i < len(lista1):
        lista_intercalada.append(lista1[i])
    if i < len(lista2):
        lista_intercalada.append(lista2[i])
print("Lista intercalada: ", lista_intercalada)