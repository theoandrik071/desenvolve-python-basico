## Escreva e execute seu código aqui
n = int(input("Quantos jogos o galo teve: "))
soma = 0
vitorias = 0
empates = 0
derrotas = 0
for jogos in range(n):
    golsgal = int(input("Quantos gols o galo fez: "))
    golsop = int(input("Quantos gols o oponente fez: "))
    if golsgal > golsop:
        soma += 3
        vitorias += 1
    elif golsgal == golsop:
        soma += 1
        empates += 1
    else:
        derrotas += 1
print(f"Vitórias: {vitorias}")
print(f"Empates: {empates}")
print(f"Derrotas: {derrotas}")
print(f"Pontuação: {soma}")