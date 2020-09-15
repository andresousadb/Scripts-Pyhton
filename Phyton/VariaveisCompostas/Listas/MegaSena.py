from random import randint
lista = list()
jogos = list()
cont = 0
print('#*' * 27)
print('\033[1;35m           JOGA NA MEGA SENA       \033[m ')
print('#*' * 27)
quant = int(input('Quantos jogos você quer que sorteie? '))
tot = 1
while tot <=quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*3,f'SORTEANDO {quant} JOGOS','-='*3)
for i,l in enumerate(jogos):
    print(f'Jogo {i+1}:{l}')
print('\033[1;33m-='*3,'BOA SORTE !','-='*3)