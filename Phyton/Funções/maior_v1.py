def maior(*num):
    cont = maior = 0
    print('Analisando sequência')
    for valor in num:
        print(f'{valor} ',end='')
        if cont == 0:
            maior = valor

        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam digitados {cont} valores')
    print(f'O maior valor é {maior}')


#PROGRAMA
maior(1, 5, 9, 7, 8, 10)
maior(1, 6, 23, 96)
maior(1, 50)
maior(10)
maior()
