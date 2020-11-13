nome = str(input('Digite o seu nome completo '))
print(' Analisando o seu nome... ')
print('O seu nome em maiuscula é {}'.format(nome.upper()))
print('O seu nome em minuscula é {}'.format(nome.lower()))
print('O seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('O seu primeiro nome tem {} letras'.format(nome.find(' ')))


