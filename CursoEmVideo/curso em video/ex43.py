peso = float(input('digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você esta ABAIXO do peso normal')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você esta na faixa do pes NORMAL')
elif 25 <= imc < 30:
    print('Você esta em SOBREPESO')
elif 30 <= imc <= 40:
    print('Você esta em OBESIDADE')
elif imc >= 40:
    print('CUIDADO, Você esta em OBESIDADE MORBIDA')
