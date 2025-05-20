Idade = int(input("Digite sua idade:"))
Jogou = (input("Já jogou pelo menos 3 jogos de tabuleiro ?")) == 'true'
Vitorias = int(input("Quantos jogos já venceu:"))
print("Apto para ingressar no clube de jogos de tabuleiro", (Idade >=16 and Idade <=18)and Jogou and (Vitorias >= 1))