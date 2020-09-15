from Erros.Sistema.lib.interface import *
from Erros.Sistema.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if arquivoexiste(arq):
    print('Arquivo encontrada com sucesso!')
else:
    print('Arquivo não encontrado')
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # opção de listar
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do Sistema...Até logo!')
        break
    else:
        print('\033[31mErro! digite um opção valida\033[m')
    sleep(2)
