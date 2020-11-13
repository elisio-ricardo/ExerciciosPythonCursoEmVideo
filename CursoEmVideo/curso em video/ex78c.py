posicao = []
maior = 0
menor = 0
for c in range(0, 5):
    n = (int(input(f'Digite um valor na posição {c + 1}: ')))
    posicao.append(n)
    if c == 0:
        maior = n
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print('-=' * 30)
print(f'Os valores digitados foram {posicao}')
print(f'O  maior valor foi {maior} ficou ', end='')
for i, v in enumerate(posicao):
    if v == maior:
        print(f'na posição {i+1}...', end='')
print()
print(f'O menor valor foi {menor} e ficou ', end='')
for i, v in enumerate(posicao):
    if v == menor:
        print(f'na posição {i + 1}...', end='')



#print(f'O maior valor foi {maior} na posiçâo {i}')
#print(f'O menor valor foi {menor} na posição {i}')
