ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        print('FINALIZANDO')
        break
print('-=' * 30)
print(f'{"N°":<4}{"NOME":<10}{"MEDIA":>8}')
print('-=' * 30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.2f}')
while True:
    print('-=' * 30)
    opc = int(input('Mostras notas de qual aluno? [999 para parar] '))
    if opc == 999:
        print('FINALIZANDO PROGRAMA')
        break
    if opc <= len(ficha) - 1:
        print(f'As Notas do aluno {ficha[opc][0]} são {ficha[opc][1]}')
print('FECHANDO')
