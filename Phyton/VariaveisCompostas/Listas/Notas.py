aluno = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1+nota2) / 2
    aluno.append([nome, [nota1, nota2],media])
    r = str(input('Quer continuar [S/N] ')).strip().upper()[0]
    if r in ('N'):
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*30)
for i, a in enumerate(aluno):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('-'*30)
while True:
    print('-='*35)
    opc = int(input('Mostrar notas de qual aluno? 999 interrompe '))
    if opc == 999:
        print('FINALIZANDO....')
        break
    if opc <= len(aluno) - 1:
        print(f'Notas de {aluno[opc][0]} são {aluno[opc][1]}')


