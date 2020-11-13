numero = int(input('Me diga um numero qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('O numero {} digitado é PAR'.format(numero))
else:
    print('O numero {} digitado é IMPAR'.format(numero))
