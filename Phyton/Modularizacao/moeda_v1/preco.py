from Modularizacao.moeda_v1 import moeda

p = float(input('Digite o preco R$ '))
print(f'A metade de {p} é {moeda.metade(p,True)}\033[m')
print(f'O dobro de {p} é {moeda.dobro(p,True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p,10,True)}')
print(f'Diminuir 5%,temos {moeda.diminuir(p,5,True)}')
