'''teste = list()
teste.append('André')
teste.append(29)

galera = list()
galera.append(teste[:])
teste[0] = 'Andresa'
teste[1] = 22
galera.append(teste[:])
print(galera)'''

'''galera = [['Joao',19],['Andre',29],['Marcio',24],['Andresa',22]]
for p in galera:
    print(f'{p[0]}.......{p[1]}')'''
galera = list()
dado = list()
totmai = totalmen = 0
for p in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for c in galera:
    if c[1] >= 21:
        print(f'{c[0]} é maior de idade')
        totmai +=1
        
    else:
        print(f'{c[0]} é menor de idade')
        totalmen +=1
print(f'temos {totmai} maiores e {totalmen} menores de idade')


