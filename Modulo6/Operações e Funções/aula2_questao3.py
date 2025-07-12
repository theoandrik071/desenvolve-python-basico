import random
list1 = []
list2 = []
interseccao = []
for i in range(20):
    list1.append(random.randint(0,50))
    list2.append(random.randint(0,50))
print("lista1 - ", list1)
print("lista2 - ", list2)

for elemento in list1:
    if elemento in list2:
        interseccao.append(elemento)
interseccao.sort()
print("intersecção - ", interseccao)
for i in interseccao:
    print(f"{i}: (Lista1={list1.count(i)}, Lista2={list2.count(i)})")
