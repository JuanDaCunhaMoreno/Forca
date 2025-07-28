import random
from interface import limpar_tela, display_hangman
from palavras import palavras_por_categoria

def game():
    limpar_tela()
    print("\nBem-Vindo(a) ao jogo da forca!")
    print("Escolha uma categoria:\n")

    categorias = list(palavras_por_categoria.keys())
    for i, cat in enumerate(categorias, 1):
        print(f"{i}. {cat}")

    escolha = input("\nDigite o número da categoria: ").strip()

    while not (escolha.isdigit() and 1 <= int(escolha) <= len(categorias)):
        escolha = input("Opção inválida. Digite o número correto da categoria: ").strip()

    categoria_escolhida = categorias[int(escolha) - 1]
    lista_palavras = palavras_por_categoria[categoria_escolhida]

    palavra = random.choice(lista_palavras)
    letras_descobertas = ["-" for _ in palavra]
    chances = len(palavra)
    letras_erradas = []

    while chances > 0:
        print("\n" + "".join(letras_descobertas))
        print(f"Chances restantes: {chances}")
        print(display_hangman(len(palavra) - chances))
        print(f"Letras erradas: {letras_erradas}")

        # Validação da entrada
        while True:
            tentativa = input("Digite uma letra: ").lower()
            if len(tentativa) != 1:
                print("⚠️  Digite apenas uma letra!")
            elif not tentativa.isalpha():
                print("⚠️  Digite somente letras, sem números ou símbolos!")
            else:
                break

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
