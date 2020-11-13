num = int(input('Qual tabuada você deseja: '))
s = 0
for c in range(1, 11):
    print(f'{num} x {c} = {c*num}')
    soma = c * num
    s += soma
print(f'E a soma de todos os resultados é {s}')