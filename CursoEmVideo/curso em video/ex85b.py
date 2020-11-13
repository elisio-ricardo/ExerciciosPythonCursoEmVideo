lista = [[], []]
for c in range(1, 8):
    valor = int(input('Digite um numero: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print(f'Os numeros pares foram {lista[0]}')
print(f'Os numeros impares foram {lista[1]}')
