import random
chute = 0
numero = 0
for i in range(1):
    rand = random.randint(1,10)
    numero = rand
while numero != chute:
    chute = int(input("Adivinhe o número entre 1 e 10: "))
    if chute == numero:
        break
    elif chute >= numero:
        print("Muito alto, tente novamente!")
    else:
        print("Muito baixo, tente novamente!")
print(f"Correto! o número é {numero}.")