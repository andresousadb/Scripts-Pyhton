num = (int(input('Digite 1° numero: ')),
      int(input('Digite 2° numero: ')),
      int(input('Digite 3° numero: ')),
      int(input('Digite 4° numero: ')))
print(f'Você digitou os valores {num}')
print(f'O numero 9 apareceu {num.count(9)} vezes')
if num == 3:
    print(f'O valor 3 apareceu na {num.index(3)} posiçao')
else:
    print('Não existe numero 3 digitado')
print('Os valores pares digitados foram ',end='')
for n in num:
    if n % 2 == 0:
        print(n,end=' ')
print('\nFIM DO PROGRAMA')



