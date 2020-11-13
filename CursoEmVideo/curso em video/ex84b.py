lista = []
final = []
pesomaior = pesomenor = 0
while True:
    lista.append(str(input('Digite o seu nome: ')))
    lista.append(int(input('Digite o seu peso: ')))
    if len(final) == 0:
        pesomaior = pesomenor = lista[1]
    else:
        if lista[1] > pesomaior:
            pesomaior = lista[1]
        if lista[1] < pesomenor:
            pesomenor = lista[1]
    final.append(lista[:])
    lista.clear()
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
print(f'total de pessoas cadastradas {len(final)}')

print(f'O maior peso foi {pesomaior} da pessoa', end=' ')
for p in final:
    if p[1] == pesomaior:
        print(f'{p[0]}', end=' ')
print()
print(f'O menor peso foi {pesomenor} da pessoa', end=' ')
for p in final:
    if p[1] == pesomenor:
        print(f'{p[0]}', end=' ')




