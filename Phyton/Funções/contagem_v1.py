

def contador (i, f, d):
    if d < 0:
        d *= -1
    if d == 0:
        d = 1
    print(f'Contagem de {i} até {f} de {d} em {d}')

    if i < f:
        cont = i
        while cont <=f:
            print(f'{cont} ', end='')
            cont += d
        print('FIM')
    else:
        if i > f:
            cont = i
            while cont >= f:
                print(f'{cont} ',end='')
                cont -= d
            print('FIM')


#PROGRAMA
contador(1, 10, 1)
contador(10, 0, 2)
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
de = int(input('De: '))
contador(ini, fim, de)
