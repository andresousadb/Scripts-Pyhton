def ficha(jog=' <desconhecido> ', g=0):
    print(f'O jogador {jog} fez {g} gol(s) no campeonato')


# programa
nome = str(input('Nome do Jogador: '))
gol = str(input('Numero de Gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    ficha(g=gol)
else:
    ficha(nome, gol)
