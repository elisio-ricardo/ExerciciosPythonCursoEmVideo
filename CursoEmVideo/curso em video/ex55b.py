maior = menor = 0
for c in range(1, 6):
    peso = float(input(f'Digite o Peso da {c}° pessoa: Kg '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso foi Kg {maior}')
print(f'O menor peso foi Kg {menor}')

