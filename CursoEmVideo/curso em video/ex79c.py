lista = []

while True:
    n = int(input('digite um valor: '))
    if n not in lista:
        lista.append(n)
    resp = str(input('Deseja continuar: [S/N]')).strip().upper()[0]
    if 'N' in resp:
        break
    while resp not in 'S':
        resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
        if 'N' in resp:
            break


lista.sort()
print(lista)
