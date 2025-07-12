print("Digite ps números inteiros (pelomenos 4), digite 'fim' para terminar:")
numeros = []
while len(numeros) < 4:
    entrada = input()
    numeros.append(int(entrada))
while True:
    entrada = input()
    if entrada.lower() == 'fim':
        break
    numeros.append(int(entrada))
print("Lista original: ",numeros)
print("Os 3 primeiros elementos: ",numeros[:3])
print("Os 2 últimos elementos: ",numeros[-2:])
print("Lista invertida: ",numeros[::-1])
print("Elementos de índice par: ",numeros[::2])
print("Elementos de índice ímpar: ",numeros[1::2])