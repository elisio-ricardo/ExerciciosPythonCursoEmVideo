salario = float(input('Digite o valor do salário do funcionário :  '))
if salario <= 1250:
    novo = salario + (salario *(15 / 100))
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava {:.2f} passara a ganhar {:.2f}'.format(salario, novo))
