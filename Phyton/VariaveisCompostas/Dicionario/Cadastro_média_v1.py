pessoas = dict()
galera = list()
media = soma = 0
while True:
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
        if pessoas['sexo'] in 'FM':
            break
        print('ERROR !!!!!!!')
    pessoas['idade'] = int(input('Idade: '))
    galera.append(pessoas.copy())
    soma += pessoas['idade']
    while True:
        r = str(input('Quer continuar? [S/N]: ')).strip().upper()
        if r in 'SN':
            break
        print('Tá doido é sim ou não !')
    if r in 'N':
        break
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'B) A média de idade é de {media} anos')
print(f'C) As mulheres cadastradas foram ', end=' ')
for g in galera:
    if g['sexo'] in 'F':
        print(f'{g["nome"]} ', end=' ')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('   ',end='')
        for i,v in p.items():
            print(f'{i} = {v}; ', end=' ')
print('<><><>ENCERRADO<><><>')








