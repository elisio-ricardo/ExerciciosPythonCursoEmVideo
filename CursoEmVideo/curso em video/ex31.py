distancia = int(input('Qual a distância da sua viagem em km ? \n '))
print('Você esta preste a iniciar uma viagem de {}km '.format(distancia))
if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45
print('E o preço da sua passagem será R${:.2f}'.format(preco))
print('Tenha uma Boa viagem')