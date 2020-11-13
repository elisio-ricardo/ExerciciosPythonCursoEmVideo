numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado.')
    else:
        print('Valor duplicado! Não adicionado.')
    r = str(input('Quer continuar ? [S/N]'))
    if r in 'Nn':
        break
numeros.sort()
print(f'Você digitou os valores {numeros}')