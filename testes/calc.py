ex = ""
n = int(input("Digite um numero: "))
soma = n
while True:
    ex = input('Digite uma expressão "+ ou -" ou Fim: ')
    if ex == 'Fim':break
    if  ex == '+' or ex == '-':
        n = int(input("Digite um numero: "))
        if ex == '+':
            soma += n
        elif ex == '-':
            soma -= n
    else:
        print("Operação invalida.")
print(soma)