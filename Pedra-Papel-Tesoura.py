import random

pontos_jogador = 0
pontos_computer = 0
numero_empates = 0

opçoes = ["pedra", "papel", "tesoura"]

while True:
    escolha = str(input("Escolha entre Pedra / Papel / Tesoura ou digite S para sair\n")).lower()
    if escolha == "s":
        break

    if escolha not in opçoes:
        print("Por favor escolha uma opção válida\n")
        continue


    aleatorio = random.randint(0, 2)
    computador = opçoes[aleatorio]
    print("O computador escolheu: ",computador)

    if escolha == "pedra" and computador == "pedra":
        print("Empate!\n")
        numero_empates += 1
    elif escolha == "pedra" and computador == "tesoura":
        print("Você ganhou essa rodada!\n")
        pontos_jogador += 1
    elif escolha == "pedra" and computador == "papel":
        print("Você perdeu essa rodada!\n")
        pontos_computer += 1

    elif escolha == "papel" and computador == "pedra":
        print("Você ganhou essa rodada!\n")
        pontos_jogador += 1
    elif escolha == "papel" and computador == "tesoura":
        print("Você perdeu essa rodada!\n")
        pontos_computer += 1
    elif escolha == "papel" and computador == "papel":
        print("Empate!\n")
        numero_empates += 1


    elif escolha == "tesoura" and computador == "pedra":
        print("Você perdeu essa rodada!\n")
        pontos_computer += 1
    elif escolha == "tesoura" and computador == "papel":
        print("Você ganhou essa rodada!\n")
        pontos_jogador += 1
    elif escolha == "tesoura" and computador == "tesoura":
        print("Empate!\n")
        numero_empates += 1



print("O seu número de vitorias foi : ",pontos_jogador)
print("O seu número de derrotas foi : ",pontos_computer)
print("O número de empates foi : ",numero_empates)

print("\nObrigado por jogar!")


