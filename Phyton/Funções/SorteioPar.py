from random import randint

def sorteia(lista):
    print('Os valores sorteados foram: ',end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ',end='')
    print('PRONTO !')

def somaParImpar(lista):
    somaP = somaI = 0
    for valor in lista:
        if valor % 2 == 0:
            somaP +=valor
        else:
            if valor % 2 ==1:
                somaI += valor
    print(f'Somando os valores impares sorteados {lista}, temos {somaI}')
    print(f'Somando os valores pares sorteados {lista}, temos {somaP}')

numeros = list()
sorteia(numeros)
somaParImpar(numeros)







# from random import randint
#
#
# def sorteio(*num):
#     for valores in num:
#         print(f'{valores} ', end='')
#
#
# # PROGRAMA
# print('Sorteando 5 valores da lista: ', end='')
# sorteio(randint(1, 10))
# sorteio(randint(1, 10))
# sorteio(randint(1, 10))
# sorteio(randint(1, 10))
# sorteio(randint(1, 10))
