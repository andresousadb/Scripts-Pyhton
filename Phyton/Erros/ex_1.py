def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: Por favor dite um numero inteiro validor\033[m')
            continue
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input('Digite um Real'))
        except(ValueError, TypeError):
            print('\033[31mErro: Por favor dite um numero Real validor\033[m')
            continue
        else:
            return n


n1 = leiaInt('Digite um Inteiro: ')
n2 = leiaFloat('Digite um Real: ')

print(f'O valor inteiro foi {n1} e o real foi {n2}')
