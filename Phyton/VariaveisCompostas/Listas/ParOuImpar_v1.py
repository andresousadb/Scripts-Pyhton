numero = list()
pares = list()
impares = list()
while True:
    n = int(input('Digite um numero: '))
    numero.append(n)
    r = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
for i,v in enumerate(numero):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('\033[1;31m-=\033[m'*30)
print(f'\033[1;33mA lista completa digitada foi {numero}\033[m')
print(f'\033[1;36mO numeros impares digitador foram {impares}\033[m')
print(f'\033[1;37mO numeros pares digitador foram {pares}\033[m')
