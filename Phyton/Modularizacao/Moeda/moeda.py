c = ('\033[m',  # 0 - SEM COR
         '\033[1;31m',  # 1 - VERMELHO
         '\033[1;32m',  # 2 - VERDE
         '\033[1;33m',  # 3 - AMARELO
         '\033[1;34m',  # 4 - AZUL
         '\033[1;35m',  # 5 - ROXO
         '\033[7;30m'  # 6 - BRANCO
         );

def aumentar(preco, taxa):
    res = preco + (preco * taxa / 100)
    print(f'{c[1]}', end='')
    return res


def diminuir(preco, taxa):
    res = preco - (preco * taxa / 100)
    print(f'{c[2]}', end='')
    return res


def dobro(preco):
    res = preco * 2
    print(f'{c[3]}', end='')
    return res


def metade(preco):
    res = preco / 2
    print(f'{c[4]}', end='')
    return res
