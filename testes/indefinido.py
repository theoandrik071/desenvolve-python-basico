valor = int(input("Digite um numero: "))
menor = valor
maior = valor
while valor != 0:
    valor = int(input("Digite um numero: "))
    if menor > valor:
        menor = valor
    if maior < valor:
        maior = valor
print(f"Maior: {maior}")
print(f"Menor: {menor}")