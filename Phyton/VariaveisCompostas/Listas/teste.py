'''
num = [1,5,9,4,6]
num[1] = 10
num.append(7)
num.sort()
#num.sort(reverse=True)
num.insert(2,0)
#num.pop()
print(num)
print(f'Essa lista tem {len(num)} elementos')
'''

'''valores = list []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posicao {c} encontrei o valor {v}!')
print('FIM')'''

'''valores = list ()
for cont in range(0,5):
        valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posicao {c} encontrei o valor {v}!')
print('FIM')'''

a = [2, 3, 4, 7]
b = a[:]
b[3] = 1
b[0] = 10
print(f'LISTA A : {a}')
print(f'LISTA B : {b}')
