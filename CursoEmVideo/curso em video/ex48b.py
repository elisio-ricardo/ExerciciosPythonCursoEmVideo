s = 0
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c, end=' ')
        s += c
        soma += 1
print(f'\nA soma dos valores são {s} e o total dos valores são {soma}')
