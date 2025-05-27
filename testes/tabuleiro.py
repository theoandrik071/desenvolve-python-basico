#Faça um programa que lê dois inteiros N e M, e imprime na tela um campo de batalha naval. O tabuleiro deve possuir N linhas e M colunas.
# A primeira linha é composta por um espaço em branco e o cabeçalho das colunas, ou seja valores de 1 a M. 
# As N linhas seguintes iniciam com o cabeçalho da linha, ou seja seu número, seguido de M caracteres "/" (barra) indicando uma possível posição jogável.
#Entrada:
#5
#4
#Saída:
#  1 2 3 4 
#1 / / / / 
#2 / / / / 
#3 / / / / 
#4 / / / / 
#5 / / / / 
#Para esse exercício, precisamos lembrar que o comando print implicitamente adiciona uma quebra de linha ao final da impressão.
#Podemos interferir no final da impressão adicionando mais uma entrada ao print. No exemplo, finalizamos cada linha com um espaço em branco:
#print("Texto qualquer", end = " ")
n = int(input("Digite o numero de linhas: "))
m = int(input("Digite o numero de colunas: "))
linha = ""
cabecalho = "  "
for colunas in range(m):
    linha += "/ "
for coluna in range(m):
    cabecalho += (f"{coluna + 1} ")
print(cabecalho)
for linha_inicio in range(n):
    print(f"{linha_inicio + 1} " + linha)