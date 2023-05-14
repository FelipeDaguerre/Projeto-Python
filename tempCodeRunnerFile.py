import random
import string


def gerar_senha(tamanho_min, numeros=True, caracteres_especiais=True):
    letras = string.ascii_letters
    digitos = string.digits
    especial = string.punctuation

    caracteres = letras
    if numeros:
        caracteres += digitos
    if caracteres_especiais:
        caracteres += especial

    senha = ""
    criterio = False
    tem_numero = False
    tem_especial = False

    while not criterio or len(senha) < tamanho_min:
        novo_char = random.choice(caracteres)
        senha += novo_char

        if novo_char in digitos:
            tem_numero = True
        elif novo_char in especial:
            tem_especial = True

        criterio = True
        if numeros:
            criterio = tem_numero
        if caracteres_especiais:
            criterio = criterio and tem_especial
    return senha

tamanho_minimo = int(input("Digite o tamanho da senha desejada (apenas integer): "))

numeros = input("A senha deve ter números (s ou n)? ").lower() == "s"
caracteres = input("A senha deve ter caracteres especiais (s ou n)? ").lower() == "s"
senha = gerar_senha(tamanho_minimo, numeros, caracteres)

print("A senha gerada foi: ",senha)

