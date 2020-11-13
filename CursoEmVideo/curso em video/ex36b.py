valorc = float(input('Qual o valor da Casa? R$ '))
salario = float(input('Qual o valor do salario? R$'))
anos = int(input('Em quantos anos deseja pagar? '))
prest = valorc / (anos * 12)
if prest > (salario * (30/100)):
    print('Fincanciamento Negado')
else:
    print('Financiamento Autorizado')
