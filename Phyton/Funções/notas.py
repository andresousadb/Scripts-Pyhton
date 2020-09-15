def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >=7:
            r['situacao'] = 'BOA'
        elif r['média'] >= 5:
            r['situacao'] = 'RAZOAVEL'
        else:
            r['situacao'] = 'RUIM'
    return r

# programa principal
resp = notas(5.5, 2.5, 8.5, sit=True)
print(resp)
