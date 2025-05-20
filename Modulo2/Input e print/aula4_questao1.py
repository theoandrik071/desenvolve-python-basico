largura = float(input("Digite a lagura:"))
comprimento = float(input("Digite o comprimento:"))
preço = float(input("Digite o preço do metro quadrado:"))
area = comprimento * largura
preco_total = preço * area
print("O terreno possui", area, "e custa R$", preco_total)