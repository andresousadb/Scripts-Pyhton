numeros = list()
pares = list()
impares = list()
while True:
    n = int(input('Digite um número: '))
    numeros.append(n)
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
for i,v in enumerate(numeros):
    if v % 2 ==0:
        pares.append(v)
    elif v % 2 ==1:
        impares.append(v)
print(f'A lista completa é {numeros}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
