
palavra = "escaravelho"
chutes = []
chances = 6

while True:


    tentativa = input("Digite uma letra: ").lower()
    chutes.append(tentativa)

    for letra in palavra:
        if letra in chutes:
            print(letra, end=" ")
        else:
            print("-", end=" ")

    if tentativa not in palavra:
        chances -= 1
        print(f"Errou, restam {chances} chances")

    venceu = True
    for letra in palavra:
        if letra not in chutes:
            venceu = False

    if chances == 0 or venceu:
        break

if venceu:
    print(f"\n\nVocê ganhou! A palavra era {palavra}")
else:
    print(f"\n\nVocê perdeu. A palavra era {palavra}")
