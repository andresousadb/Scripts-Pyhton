numeros = list()
while True:
    n = int(input('Digite um valor: '))
    numeros.append(n)
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('-='*30)
numeros.sort(reverse=True)
print(f'Você digitou {len(numeros)} elementos.')
print(f'Os valores em ordem decrescente são {numeros}')
if 5 in numeros:
    print('O valor 5 foi encontrado na lista !')
else:
    print('O valor 5 não foi encontrado na lista !')


