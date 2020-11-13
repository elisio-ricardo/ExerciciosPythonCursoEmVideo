num = int(input('Digite um numero [999 para parar]: '))
soma = 0
tot = 0
while num != 999:
    soma += num
    tot += 1
    num = int(input('Digite um numero [999 para parar] : '))
print(f'{soma} e {tot}')