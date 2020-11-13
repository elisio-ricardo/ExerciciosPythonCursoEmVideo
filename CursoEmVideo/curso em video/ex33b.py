n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
n3 = int(input('Terceiro numero: '))
if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n3 and n2 > n1:
    maior = n2
else:
    maior = n3
if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n3 and n2 < n1:
    menor = n2
else:
    menor = n3

print(f'O menor valor {menor}')
print(f'O maior valor foi {maior}')
