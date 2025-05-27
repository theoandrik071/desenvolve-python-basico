valor = int(input("Digite um numero: "))
while valor < 0:
    valor = int(input("Digite um numero: "))
produto = valor
while valor != 0:
    valor = int(input("Digite um numero: "))
    if valor > 0:
        produto *= valor
print(f"Produto: {produto}")