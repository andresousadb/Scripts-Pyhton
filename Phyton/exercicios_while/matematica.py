p = int(input('Primeiro valor: '))
s = int(input('Segundo valor: '))
opcao = 0
maior = 0
while opcao != 5:
    print('''[1] Somar
[2] mutiplicar
[3] maior
[4] novos números
[5] sair do programa''')
    opcao = int(input('>>>>>> Qual é a sua opcão? '))
    if opcao == 1:
        print('O Resultado da soma de {} + {}={}'.format(p,s,p+s))
        print('*=*'*20)
    elif opcao == 2:
        print('O Resultado da multiplicação de {} * {}={}'.format(p,s,p*s))
    elif opcao == 3:
        if p > s:
            maior = p
        else:
            maior = s
        print('O maior entre {} e {} é {}'.format(p,s,maior))
    elif opcao == 4:
        print('Digite novos valores: ')
        p = int(input('Primeiro valor: '))
        s = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Saindo')
    else:
        print('Oção invalida.Tente novamente')
    print('=-=' * 10)
    print('Volte sempre !!!')




