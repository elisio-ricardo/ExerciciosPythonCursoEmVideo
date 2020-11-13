from random import randint
pc = randint(0, 100)
tot = 0
while True:
    num = int(input('Digite um valor: '))
    resul = pc + num
    resp = ' '
    if num == 0:
        break
    while resp not in 'IiPp':
        resp = str(input('Par ou impar? [P/I] ')).upper().strip()[0]
    print('-=' * 30)
    print(f'Voce jogou {num} e o computador {pc} o total foi {resul}', end=' ')
    print('DEU PAR' if resul % 2 == 0 else 'DEU IMPAR')
    print('-=' * 30)
    if resp in 'Ii':
        if resul % 2 == 0:
            print('Você Perdeu !!!')
            break
        else:
            print('Você Ganhou !!!')
    elif resp in 'Pp':
        if resul % 2 == 0:
            print('Você Ganhou !!!')
        else:
            print('Você Perdeu !!!')
            break

    tot += 1
print('-=' * 30)
print(f'GAME OVER!! Venceu um total de {tot} vezes')

