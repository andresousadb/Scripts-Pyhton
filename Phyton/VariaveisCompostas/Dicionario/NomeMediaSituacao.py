dados = dict()
dados['Nome'] = str(input('Nome: '))
dados['Média'] = float(input(f'Média de {dados["Nome"]}: '))
if dados['Média'] >= 7:
    dados['Situacao'] = 'Aprovado'
elif 5 <= dados ['Média'] < 7:
    dados['Situacao'] = 'Recuperacao'
else:
    dados['Situacao']  = 'Reprovado'
print('-='*30)
print('             O RESULTADO É'    )
print('-='*30)
for k,v in dados.items():
        print(f'{k} é igual a {v}')



