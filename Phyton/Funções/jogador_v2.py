def ficha(n='<desconhecido>', gols=0):
    print(f'O jogador {n},fez {g} gol(s)')


# programa
n = str(input('Nome do jogador: '))
g = str(input('Quantidade de gol(s): '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
