s = 0
i = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c} valor: '))
    if num % 2 == 0:
        s += num
    else:
        i += num

print(f'A soma dos valores pares foi {s}')
print(f'A soma dos numeros impares foi {i}')
