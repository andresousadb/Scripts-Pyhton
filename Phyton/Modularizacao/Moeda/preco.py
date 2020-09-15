from Modularizacao.Moeda import moeda

p = float(input('Digite o preco R$ '))
print(f'A metade de {p} é {moeda.metade(p)}\033[m')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p,10)}')
print(f'Diminuir 5%,temos R$ {moeda.diminuir(p,5)}')
