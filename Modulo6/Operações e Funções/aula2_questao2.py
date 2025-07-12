import random
num_elementos = random.randint(5,20)
elementos = [random.randint(1,10) for i in range(num_elementos)]
soma = 0
for numero in elementos:
    soma += numero
media = soma / num_elementos
print("Lista de elementos:", elementos)
print("Soma dos valores:", soma)
print("Media dos valores:", media)