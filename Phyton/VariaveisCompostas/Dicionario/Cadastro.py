from datetime import datetime
dados = dict()
dados ['Nome'] = str(input('Nome: '))
nasc =  int(input(f'Ano de Nascimento de {dados["Nome"]}: '))
dados ['idade'] = datetime.now().year - nasc
dados ['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados ['ctps'] == 0:
   dados ['ctps'] = '0'
elif dados ['ctps'] >= 1:
     dados['contratacao'] = int(input('Ano de contrataçao: '))
     dados ['salario'] = float(input('Salário: R$ '))
     dados['Aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
print('-='*30)
for i,k in dados.items():
    print(f'{i} tem o valor {k}')

