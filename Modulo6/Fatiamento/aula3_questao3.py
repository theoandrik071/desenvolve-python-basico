import random
lista = [random.randint(-10, 10) for _ in range(20)]
print("Original: ", lista)
tamintervalo = 3
maiorqntneg = 0
iniciomaiorintervalo = 0
for i in range(len(lista) - tamintervalo + 1):
    intervalo = lista[i:i + tamintervalo]
    qntneg = sum(1 for n in intervalo if n < 0)
    if qntneg > maiorqntneg:
        maiorqntneg = qntneg
        iniciomaiorintervalo = i
del lista[iniciomaiorintervalo:iniciomaiorintervalo + tamintervalo]
print("Editada: ", lista)