from Phyton.Jogos.interface import *
from random import randint
from time import sleep
print('*'*34)
cabecalho()
print('*'*34)
tentativas = 0

while True:
    computador = randint(1, 10)
    tentativas += 1
    jogador = int(input('Escolha um numero: '))
    if computador == jogador:
       # sleep(0.5)
        print(f'Você acertou depois de {tentativas} tentativas !!! O computador jogou {computador} !!!!!')
        break
    else:
       # sleep(0.5)
        print(f'Tente novamente ! O computador jogou {computador}')
        if jogador < computador:
            print('Número maior')
        else:
            print('Numero menor')
final()

