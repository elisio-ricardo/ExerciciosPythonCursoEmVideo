print('Gerador de P.A: ')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da P.A: '))
termo = primeiro
cont = 1
while cont <= 10:
    termo += razao
    cont += 1
    print('{}'.format(termo), end= ' ')
print('FIM')
