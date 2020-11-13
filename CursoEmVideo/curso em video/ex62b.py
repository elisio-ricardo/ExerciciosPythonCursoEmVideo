a = int(input('Qual o primeiro termo: '))
ra = int(input('Qual a razão : '))
n = 1
soma = 0
termo = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while n <= total:
        print(f'{a}', end=' ')
        a += ra
        n += 1
    print('')
    mais = int(input('Mais quantos termos deseja: '))
print(f'O total de termos foi {total}')

