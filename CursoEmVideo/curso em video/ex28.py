from random import randint
from time import sleep
computador = randint(0, 5) # faz o computador sortear um numero
print('-=-'*20) # faz um efeito de linha multiplicando 20 vx
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que numero eu pensei ? ')) # o jogador chuta um numero
print('PROCESSANDO...')
sleep(2) # comando que faz o programa aguardar X segundos
if jogador == computador:
    print('Parabens voce acertou !!')
else:
    print('ERROU... Eu pensei no número {} e Você no {} ! Tente de novo se quiser !'.format(computador, jogador))