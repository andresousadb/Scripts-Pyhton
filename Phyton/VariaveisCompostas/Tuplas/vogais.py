listagem = ('Borracha','Lapis','Caderno','Apontador')
print('='*30)
print(f'{"VOGAIS":^30}')
print('='*30)
for c in listagem:
    print('\nNa palavra',c.upper(),f'as vogais são ',end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

