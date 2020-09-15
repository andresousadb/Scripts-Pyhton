from random import randint
print('=-'*30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*30)
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint (0,11)
    escolhe = ' '
    total = jogador + computador
    while escolhe not in 'PI':
        escolhe = str(input('Escolha par ou imprar [P/I]: ')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador {computador} no total de {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if escolhe == 'P':
        if total % 2 == 0:
            print('\033[1;32mVocê ganhou\033[m')
            v += 1
        else:
            print('\033[1;31mVocê perdeu\033[m')
            break
    elif escolhe == 'I':
        if total % 2 ==1:
            print('\033[1;32mVocê ganhou\033[m')
            v +=1
        else:
            print('\033[1;31mVocê perdeu\033[m')
            break
    print('Vamos jogar novamente....')
print(f'Gamer over ! você venceu {v} vezes')

