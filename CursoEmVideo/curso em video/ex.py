from random import randint
pc = randint(1, 10)
tot = 10
while tot > 0:
    tot -= 1
    jog = int(input('Chute um numeto entre 1 e 10: [você tem 10 chances] '))

    if jog < pc:
        print(f'O numero é maior! você tem N°{tot} chances')
        print('-=' * 30)
    elif jog > pc:
        print(f'O numero é menor! você tem N°{tot} chances')
        print('-=' * 30)
    else:
        print(f'Você acertou. Voce jogou {jog} e o computador {pc}')
        break
print('AS TENTATIVAS ACABARAM! VOCÊ NÃO CONSEGUIU TENTE DENOVO')