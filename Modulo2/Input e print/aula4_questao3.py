total = 0.0
nome = input(f"Digite o nome do produto: ")
precounitario = float(input("Digite o preço unitário do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))
subtotal = precounitario * quantidade
total += subtotal
print(f"Total: R${total:,.2f}")