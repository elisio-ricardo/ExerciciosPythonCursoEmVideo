num = soma = tot = media = 0
maior = menor = 0
resp = 's'
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    tot += 1
    media = soma / tot
    if tot == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] '))

print(f'A soma é {soma} o Maior é {maior} e o menor é {menor} ')
print(f'O total de numeros foi {tot} e a media foi {media}')