print('-=' * 30)
print('CADASTRO DE PESSOAS')
print('-=' * 30)
soma18 = somah = somam = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [F/M] ')).upper().strip()[0]
    while sexo not in 'FM':
        sexo = str(input('Sexo: [F/M] ')).upper().strip()[0]
    if idade >= 18:
        soma18 += 1
    if sexo == 'M':
        somah += 1
    if sexo in 'F' and idade < 18:
        somam += 1
    print('-=' * 30)
    resp = str(input('Quer continuar [S/N] ')).upper().strip()[0]
    print('-=' * 30)
    if resp == 'N':
        break
print(f'Total Homens é {somah}')
print(f'Pessoas com mais de 18 é {soma18}')
print(f'Total mulheres menos de 18 é {somam}')
print('FINALIZANDO PROGRAMA')

