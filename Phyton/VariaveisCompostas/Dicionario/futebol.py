jogador = dict()
jogador['nome'] = str(input('Nome do jogador: '))
total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
partida = list()
for c in range(1,total+1):
    partida.append(int(input(f'Quantos gols na partida {c}: ')))
jogador['gols'] = partida[:]
jogador ['total'] = sum(partida)
print('-='*30)
print(jogador)
print('-='*30)
for k ,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
part = 0
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i,v in enumerate(jogador["gols"]):
    print(f'=> Na partida {i} fez {v} gols')



