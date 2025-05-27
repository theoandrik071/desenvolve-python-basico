import random
import math
soma = 0
n = int(input("Digite um numero: "))
for i in range(n):
        ran = (random.randint(0,100))
        print(ran)
        soma += ran
print(math.sqrt(soma))
