galera = list()
pessoas = dict()
soma = media = 0
while True:
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    galera.append(pessoas.copy())
    while True:
        re = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
        if re in 'SN':
            break
        print('Erro')
    if re == 'N':
        break
print('-='*30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A média de idade é de {media:5.2f} anos')
print(f'As mulheres cadastradas foram ',end='')
for p in galera:
    if p ['sexo'] in 'F':
        print(f'{p["nome"]} ', end='')
print()
print('Lista das pessoas que estão acima da média: ')
for p in galera:
    if p ['idade'] >= media:
        print('   ', end='')
        for k , v in p.items():
            print(f'{k} = {v}; ', end=' ')
print('<< ENCERRADO >>')

