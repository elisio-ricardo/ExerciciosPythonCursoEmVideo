tot = soma = 0
while True:
    num = int(input('Digite um numero [999 para parar]: '))
    if num == 999:
        break
    tot += 1
    soma += num
print(f'A soma dos valores foi {soma} e voce digitou {tot} numeros')
