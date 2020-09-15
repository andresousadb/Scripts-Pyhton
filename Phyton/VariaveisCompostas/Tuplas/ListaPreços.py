listagem = ('Borracha',10.90,
            'Lapis',2,
            'Caderno',11.90,
            'Apontador',0.50,
            'A4',35,
            'cartolinha',0.30,
            'teclado',99,
            'Monitor',180,
            'Mouse',45,
            'Sacola',1)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for c in range(0,len(listagem)):
    if c % 2 == 0:
        print(f'{listagem[c]:.<30}',end='')
    else:
        print(f' R$ {listagem[c]:.2f}')
