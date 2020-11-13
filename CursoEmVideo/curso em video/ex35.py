print('-='*20)
print('Analisador de triangulos')
print('-='*20)
a = float(input('Digite o primeiro lado do triangulo '))
b = float(input('Digite o segundo lado do triangulo '))
c = float(input('Digite o terceiro lado do triangulo '))
if a < b + c and b < a + c and c < b + a :
    print('Os segmentos PODEM formar um triangulo')
else:
    print('Os segmentos NÃO PODEM formar um triangulo')
