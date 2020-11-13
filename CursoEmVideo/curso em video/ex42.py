r1 = float(input('Digite o primeiro lado: '))
r2 = float(input('Digite o segundo lado: '))
r3 = float(input('Digite o terceiro lado: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('\033[31mEQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('\033[31mESCALENO')
    else:
        print('\033[31mISÔSCELES')
else:
    print('Os segmentos não podem formar um triâgulo !')