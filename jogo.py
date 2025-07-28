import random
from interface import limpar_tela, display_hangman
from palavras import palavras

def game():
    limpar_tela()
    print("\nBem-Vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")

    palavra = random.choice(palavras)
    letras_descobertas = ["-" for _ in palavra]
    chances = len(palavra)
    letras_erradas = []

    while chances > 0:
        print("".join(letras_descobertas))
        print(f"\nChances restantes: {chances}")
        print(display_hangman(len(palavra) - chances))
        print(f"Letras erradas: {letras_erradas}")
        tentativa = input("\nDigite uma letra: ").lower()

        if tentativa in palavra:
            for index, letra in enumerate(palavra):
                if tentativa == letra:
                    letras_descobertas[index] = letra
        else:
            if tentativa not in letras_erradas:
                chances -= 1
                letras_erradas.append(tentativa)

        if "-" not in letras_descobertas:
            print(f"\nVocê venceu! A palavra era: {palavra}")
            break

    if "-" in letras_descobertas:
        print(display_hangman(0))
        print(f"\nVocê perdeu! A palavra era: {palavra}")
