print('-'*30)
print('LOJA TAGADAGADA')
print('-'*30)
total = produto = menor = cont = 0
barato = ''

while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco
    if preco > 1000.00:
        produto += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    resp = ' '
    while resp not in ('SN'):
        resp = str(input('Quer continuar comprando ? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra foi de de R$ {total}')
print(f'Temos {produto} produto custando mais de R$ 1000.00')
print(f'O produto mais barato foi a {barato} que custa R${menor}')

