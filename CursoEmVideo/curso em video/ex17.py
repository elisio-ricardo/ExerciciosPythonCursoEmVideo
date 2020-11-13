from math import hypot


def hipo(cato, cata):
    hipot = hypot(cata, cato)
    print(f'Os catetos foram {cato} e {cata} e a hipotenusa no valor de {hipot}')


cato = int(input('Digite o valor do cateto OPOSTO: '))
cata = int(input('Digite o valor do cateto ADJASCENTE: '))
hipo(cato, cata)

