from math import sin, cos, tan

def angulos(an):
    seno = sin(an)
    coss = cos(an)
    tang = tan(an)
    print(f'O valor do seno é [{seno:.3f}] do cosseno é [{coss:.3f}] e da tangente é [{tang:.3f}]')


angulo = int(input('Digite o valor do angulo: '))
angulos(angulo)
