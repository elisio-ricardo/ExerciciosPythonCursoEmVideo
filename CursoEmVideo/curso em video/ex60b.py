num = int(input('Digite um numero: '))
f = 1
print(f'Calculando {num}!= ', end='')
while num > 0:
    print(f'{num}', end=' ')
    if num > 1:
        print('x ', end= '')
    f *= num
    num -= 1
print(f'= {f}')

