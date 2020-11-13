num = int(input('Digite um numero: '))
u = num // 1 % 10
d = num // 10 % 10 # // fica com a parte inteira, % fica com o resto da divisão
c = num // 100 % 10 # 1234 // 100 = 12,34. mas só vai usar o 12. 12 % 10 = 1.2 mas só vai usar o 2
m = num // 1000 % 10
print('Analisando o numero {}'.format(num))
print('A unidade é {}'.format(u))
print('A dezena é {}'.format(d))
print('A centena é {}'.format(c))
print('A milhar é {}'.format(m))

