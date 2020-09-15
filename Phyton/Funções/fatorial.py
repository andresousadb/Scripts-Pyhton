def fatorial(n, show = False):
    """
    -> calcula o fatorial de um numero
    :param n: numero do calculo
    :param show: mostra ou nao
    :return: valor
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c,end='')
            if c > 1:
                print(' X ',end='')
            else:
                print(f' = ',end='' )
        f *= c
    return f

#programa

#print(fatorial(5,show = True))
help(fatorial)