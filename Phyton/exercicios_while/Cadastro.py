tot18 = homens = mulheres = 0
while True:
    print('='*30)
    print(' CADASTRO DE PESSOAS ')
    print('='* 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('[M/F]: ')).strip().upper()[0]
    if idade >=18:
        tot18 +=1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres +=1
    resp = ' '
    while resp not in 'SN':
        resp = str (input('Quer continuar ? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Quantidade de pessoas com mais de 18 anos : {tot18}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos')

