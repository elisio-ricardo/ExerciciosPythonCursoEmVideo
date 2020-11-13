from random import randint
jog = int(input('Arrisque um numero: '))
comp = randint(1, 10)
tot = 1
while jog != comp:
    print('Errou tente novamente!!')
    jog = int(input('Arrique um numero: '))
    tot += 1
    if jog < comp:
        print('Um pouco mais')
    if jog > comp:
         print('Um pouco menos')
print(f'Parabens você acertou o computador jogou {comp} e você {jog}')
print(f'Voce acertou em {tot} tentativas')
