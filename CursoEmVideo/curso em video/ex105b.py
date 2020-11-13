def notas(*n, sit=False):
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['Situação'] = 'BOA'
        elif r['media'] >= 5:
            r['Situação'] = 'RAZOAVEL'
        else:
            r['Situação'] = 'RUIM'
    return r


resp = notas(5.5, 6.8, 7, sit=True)
print(resp)
