numero = [[],[]]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor % 2 ==0:
        numero[0].append(valor)
        pares = valor
    else:
        numero[1].append(valor)
print('-='*30)
numero[0].sort()
numero[1].sort()
print(f'valores pares digitados foram {numero[0]}')
print(f'valores impares digitador foram {numero[1]}')


