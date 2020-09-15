numeros = list()
while True:
    num = int(input('Digite um valor: '))
    if num not in numeros:
        numeros.append(num)
        print('Adicionado com Sucesso')
    else:
        print('Esse numero já existe !')
    r = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break
print(f'O valor digitados foram {sorted(numeros)}')