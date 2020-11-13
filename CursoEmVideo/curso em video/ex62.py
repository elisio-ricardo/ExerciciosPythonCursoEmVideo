print('Gerador de P.A: ')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da P.A: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais!=0:
    total = total + mais
    while cont <= total:
        termo += razao
        cont += 1
        print('{}'.format(termo), end= ' ')
    print('PAUSA')
    mais = int(input('Quantos termos você qier mostrar a mais? '))
print('Progressão finalizada com {} termos'.format(total))