import random
lista = []
for i in range(20):
    n = random.randint(-100,100)
    lista += [n]
print(lista)
lista.sort()
print(lista)
print(max(lista))
print(min(lista))