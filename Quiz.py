pontos = 0

print("Vamos Jogar! \n\n")

resposta = input("Qual é a flor nacional do Japão? ").lower()
if resposta == "flor de cerejeira":
    print("Você acertou!\n")
    pontos += 1
else:
    print("Resposta Errada!\n")

resposta = input("Qual é a gíria usada pelos locais para se referir a cidade de Nova York? ").lower()
if resposta == "gotham":
    print("Você acertou!\n")
    pontos += 1
else:
    print("Resposta Errada!\n")

resposta = input("Quantos dias são necessários para a Terra orbitar o sol? ").lower()
if resposta == "365":
    print("Você acertou!\n")
    pontos += 1
else:
    print("Resposta Errada!\n")

resposta = input("Qual é o animal nacional da Austrália? ").lower()
if resposta == "canguru vermelho":
    print("Você acertou!\n")
    pontos += 1
else:
    print("Resposta Errada!\n")

resposta = input("Qual artista pintou o teto da Capela Sistina, em Roma? ").lower()
if resposta == "michelangelo":
    print("Você acertou!\n")
    pontos += 1
else:
    print("Resposta Errada!\n")

resposta = input("Qual é o menor país do mundo? ").lower()
if resposta == "vaticano":
    print("Você acertou!\n")
    pontos += 1
else:
    print("Resposta Errada!\n")

if pontos == 1:
    print("Sua pontuação foi de 1 ponto!")
else:
    print(f"Sua pontuação foi de {pontos} pontos!: ")

continuar = input("Quer continuar jogando? Para continuar digite (sim), ou digite qualquer outra coisa para sair. ")

if continuar.lower() != "sim":
    print("Obrigado por jogar!")
    quit()
