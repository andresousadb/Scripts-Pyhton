def notas(*n, situa=False):
    """
    -> programa de notas
    :param n: uma ou mais notas
    :param situa: valor opcional
    :return: dicionario
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if situa:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOAVEL'
        else:
            r['situacao'] = 'RUIM'

    return r


# programa principal
resp = notas(5.5, 2.8, 9.8, situa=True)
print(resp)
help(notas)

