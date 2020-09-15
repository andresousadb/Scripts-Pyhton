def jogar():
    print('*' * 41)
    print('****** Bem-vindo ao jogo da Forca *******')
    print('*' * 41)

    palavra_secreta = "maça".upper()
    # LISTAS
    letras_acertadas = ['_' for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not acertou and not enforcou):
        chute = str(input('Qual letra? ')).strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                # print(f'Encontrei a letra {chute} na posicao {index}')
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print('Você ganhou !!!!')
    else:
        print('Perdeuuuu !')

    print("Fim do jogo")


if (__name__ == '__main__'):
    jogar()
