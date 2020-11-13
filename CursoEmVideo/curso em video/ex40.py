n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if n1 > 10 or n2 > 10:
    print('Digite notas validas')
elif 10 >= media >= 7:
    print(' A sua primeira nota foi {} e a segunda nota foi {} então a sua media é {}'.format(n1, n2, media))
    print(' \033[32mAPROVADO\033[m!')
elif 7 > media >= 5:
    print(' A sua primeira nota foi {} e a segunda nota foi {} então a sua media é {}'.format(n1, n2, media))
    print(' \033[33mRECUPERAÇÃO\033[m!')
else:
    print('A sua primeira nota foi {} e a segunda nota foi {} entao a sua media é {}'.format(n1, n2, media))
    print('\033[31mREPROVADO\033[m!')