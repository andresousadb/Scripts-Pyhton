c = ('\033[m',  # 0 - SEM COR
         '\033[1;31m',  # 1 - VERMELHO
         '\033[1;32m',  # 2 - VERDE
         '\033[1;33m',  # 3 - AMARELO
         '\033[1;34m',  # 4 - AZUL
         '\033[1;35m',  # 5 - ROXO
         '\033[7;30m'  # 6 - BRANCO
         );

def aumentar(preco=0, taxa=0,formato=False):
    res = preco + (preco * taxa / 100)
    print(f'{c[1]}', end='')
    return res if formato is False else moeda(res)


def diminuir(preco, taxa,formato=False):
    res = preco - (preco * taxa / 100)
    print(f'{c[2]}', end='')
    return res if formato is False else moeda(res)


def dobro(preco=0,formato=False):
    res = preco * 2
    print(f'{c[3]}', end='')
    return res if formato is False else moeda(res)


def metade(preco=0,formato=False):
    res = preco / 2
    print(f'{c[4]}', end='')
    return res if formato is False else moeda(res)

def moeda(preco=0,moeda = 'R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')


def resumo(preco=0,taxaa=10,taxar=5):
    print(f'{c[2]}',end='')
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'PRECO ANALISADO: \t{moeda(preco)}')
    print(f'DOBRO DO PRECO: \t{dobro(preco,True)}')
    print(f'METADE DO PREÇO: \t{metade(preco,True)}')
    print(f'Com {taxaa} de aumento: \t{aumentar(preco,taxaa,True)}')
    print(f'Com {taxar}% de redução: {diminuir(preco,taxar,True)}')

    print('-'*30)

