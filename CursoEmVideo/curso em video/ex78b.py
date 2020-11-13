valor = []
maior = menor = 0
for c in range(0, 5):
    valor.append(int(input(f'Digite o {c + 1}° valor: ')))
    if c == 0:
        maior = menor = valor[c]
    else:
        if valor[c] > maior:
            maior = valor[c]
        if valor[c] < menor:
            menor = valor[c]

print(f'A sua lista foi {valor}')
#print(f'O maior valor é {maior}', end=' ')
for i, v in enumerate(valor):
    if v == maior:
        print(f'O maior valor é {v} na posição {i + 1}')
for i, v in enumerate(valor):
    if v == menor:
        print(f'O menor valor é {v} na posicão {i + 1}')
#print(f'O menor valor é {menor}')
