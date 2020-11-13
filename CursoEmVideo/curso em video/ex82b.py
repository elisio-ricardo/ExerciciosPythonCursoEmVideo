lista = []
pares = []
impares = []
while True:
    n = int(input('Digite um numero: '))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    if n % 2 == 1:
        impares.append(n)

    if resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]'))
    if resp == 'N':
        break
print(f'{lista}')
print(f'Os numeros impares foram {impares}')
print(f'Os numeros pares foram {pares}')
