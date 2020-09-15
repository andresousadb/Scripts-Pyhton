from datetime import date
dataAtual =  date.today().year
ano = int(input('Ano de nascimento : '))
idade = dataAtual - ano
if idade == 18:
    print('Você precisa se alistar imediatamento !!!!!!!!!!!!')
elif idade < 18:
    alistamento = 18 - idade
    dataAlis = dataAtual + alistamento
    print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, dataAtual))
    print('Ainda faltam {} anos para seu alistamento\nSeu alistamento será em {}'.format(alistamento,dataAlis))
else:
    alistamento = idade - 18
    dataAlis = dataAtual - alistamento
    print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, dataAtual))
    print('Você já deveria ter se alistado há {} anos\nSeu alistamento foi em {}'.format(alistamento,dataAlis))
