'''import math
angulo = float(input(' Digite o angulo que voce deseja: '))
seno = math.sin(math.radians(angulo))
print ('O angulo de {} tem o seno de {:.2f}'.format(angulo, seno))
coseno = math.cos(math.radians(angulo))
print('O Angulo de {} tem o coseno de {:.2f}'.format(angulo, coseno))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem a tangente de {}'.format(angulo, tangente))'''

from math import radians, cos, sin, tan
angulo = float(input(' Digite o angulo  '))
seno = sin(radians(angulo))
print(' O angulo de {} tem o seno de {}'.format(angulo, seno))
coseno = cos(radians(angulo))
print ('O angulo de {} tem o coseno de {}'.format(angulo, coseno))
tangente = tan(radians(angulo))
print('O angulo de {} tem a tangente de {}'.format(angulo, tangente))
