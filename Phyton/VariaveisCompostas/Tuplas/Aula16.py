'''lanche = ('hambuguer', 'suco', 'pizza', 'pudim', 'batata-frita')
#tuplas são imutavies
for comida in lanche:
    print(f'Eu vou comer {comida}')
print(f'Comi muito caramba foram {len(lanche)} itens gostosos')'''

lanche = ('hambuguer', 'suco', 'pizza', 'pudim', 'batata-frita')
for con in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[con]} na posicao {con}')
print(f'Estou cheio foram {len(lanche)} lanches ')

