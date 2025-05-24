n = int(input("Digite o número de respondentes: "))
if n <= 0:    print("Número inválido de respondentes!")
else:    
    soma_idades = 0    
    contador = 1
while contador <= n:
    print("Digite a idade do respondente", contador, end=": ")
    idade = int(input())
    soma_idades = soma_idades + idade
    contador = contador + 1
media = soma_idades / n
print("A média de idade dos respondentes é:", media, "anos")