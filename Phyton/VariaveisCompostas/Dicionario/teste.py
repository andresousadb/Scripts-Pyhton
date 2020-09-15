"""pessoas = {'Nome':'André','Sexo':'M','idade':29}
pessoas ['peso'] = 81
#print(f'O {pessoas["Nome"]} tem {pessoas["idade"]} anos ')
#print(pessoas.items())
for k,v in pessoas.items():
    print(f'{k}...{v}')
brasil = []
estado = {'uf':'Rio de Janeiro','sigla':'RJ'}
estado2 = {'uf':'Sao paulo','sigla':'SP'}
brasil.append(estado)
brasil.append(estado2)

print(brasil[0]['sigla'])"""

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k,v in e.items():
        print(f'O campo {k} tem valor {v}.')
