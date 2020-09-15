time = list()
jogador = dict()
partida = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partida.clear()
    for c in range(1,total+1):
        partida.append(int(input(f'Quantos gols na partida {c}: ')))
    jogador['gols'] = partida[:]
    jogador['total'] = sum(partida)
    time.append(jogador.copy())
    while True:
        r = str(input('Quer continar? [S/N]')).strip().upper()
        if r in 'SN':
            break
        print('Opa!!! Resposta Invalida !')
    if r == 'N':
        break
print('-'*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, i in enumerate(time):
    print(f'{k:>4}', end=' ')
    for d in i.values():
        print(f'{str(d):<15}', end=' ')
    print()
print('-'* 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? 999 para parar '))
    if busca == 999:
        break
    if busca >= len(time):
        print('Não existe na buscar')
    else:
        print(f'-- levantamento do jogador {time[busca]["nome"]}: ')
        for i,g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols')
    print('-' * 40)
print('XAU')






