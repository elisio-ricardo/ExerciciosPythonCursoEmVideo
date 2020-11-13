from random import randint
from time import sleep


def spa():
    print('~-' * 40)


pc = randint(0, 6)
spa()
print('Vou pensar em um numero de 0 a 6 tente adivinhar !!')
spa()
num = int(input('Digite um palpite: '))
spa()
while True:
    if num == pc:
        sleep(2)
        print(f'Você Veceu eu pensei em {pc} e você {num}')
        break
    else:
        print(f'Você perdeu eu pensei em {pc} e você {num}')
        spa()
        resp = str(input('Vamos novamente ? [S/N] '))
        if resp in 'Ss':
            num = int(input('Digite um palpite: '))
        else:
            break
spa()
print("ATE LOGO FIM")
spa()


