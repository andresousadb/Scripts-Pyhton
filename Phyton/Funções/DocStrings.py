def contador(i,f,p):
    """
     -> Faz uma contagem e mostra na tela
    :param i:Inicio
    :param f:Fim
    :param p:passo da contagem
    :return:sem retorno

    """
    c = 1
    while c <=f:
        print(f'{c} ',end='')
        c+=p
    print('FIM')

#programa
contador(2,10,2)

#help(contador)