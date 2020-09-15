def numeros(*num):
    cont = maior = menor = 0
    print('Maiores e Menores numeros: ', end='')
    for valores in num:
        print(f'{valores} ', end='')
        if cont == 0:
            valores = maior
        else:
            if valores > maior:
                maior = valores
        cont += 1
    print(f'\nA quantidade de numeros é {cont}')
    print(f'O maior valor foi {maior}')
    print(f'O menor valor foi {min(num)}')


# PROGRAMA
numeros(1, 9, 8, 3, 2, 4)
