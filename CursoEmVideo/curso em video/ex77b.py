palavras = ('Cadeira', 'Mesa', 'Geladeira', 'Cama', 'Colchão')
for p in palavras:
    print(f'\n{p}', end=' ')
    for v in p:
        if v in 'aeiou':
            print(f' {v}', end=' ')
