maisv = menos20 = 0
idadet = 0
nomeh = 0
for p in range(1, 5):
    nome = str(input(f'Digite o nome da {p}° pessoa: '))
    idade = int(input('Digite a sua idade: '))
    idadet += idade
    media = idadet / 4
    sexo = str(input('Diga o seu sexo: [F/M]')).upper().strip()[0]
    print('=-' * 30)
    if p == 1 and sexo in 'Mm':
        maisv = idade
        nomeh = nome
    if idade > maisv and sexo in 'Mm':
        maisv = idade
        nomeh = nome
    if sexo in 'Ff' and idade < 20:
        menos20 += 1

print(f'A media das idades é {media}')
print(f'O homen mais velho tem a idade de {maisv} anos e seu nome é {nomeh}')
print(f'o total de mulheres com menos de 20 anos é {menos20}')
