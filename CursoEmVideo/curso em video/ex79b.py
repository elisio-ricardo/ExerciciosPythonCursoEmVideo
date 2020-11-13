num = []
while True:
    n = (int(input('Digite um valor: ')))
    if n not in num:
        num.append(n)
        print('Valor Adicionado com sucesso...')
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    else:
        print('Valor já existente, não adicionado..')
    if resp == 'N':
        break
    if resp != 'S':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

print(f'{sorted(num)}')
