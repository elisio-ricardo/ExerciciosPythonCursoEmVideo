listagem = ('lapis', 2, 'caderno', 30.00, 'livro', 50.00, 'borracha', 3.00)
print('-=' * 30)
for lis in range(0, len(listagem)):
    if lis % 2 == 0:
        print(f'{listagem[lis]:.<20}', end=' ')
    else:
        print(f'{listagem[lis]:>5.2f}')
