c = ('\033[m',  # 0 - SEM COR
         '\033[1;31m',  # 1 - VERMELHO
         '\033[1;32m',  # 2 - VERDE
         '\033[1;33m',  # 3 - AMARELO
         '\033[1;34m',  # 4 - AZUL
         '\033[1;35m',  # 5 - ROXO
         '\033[7;30m'  # 6 - BRANCO
         );

def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'{c[1]}', end='')
            print(f'ERRO: \"{entrada}\" é um Preco INVALIDO')
        else:
            valido = True
            return float(entrada)