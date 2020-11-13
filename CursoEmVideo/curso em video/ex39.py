from datetime import date
anoN = int(input('Digite o seu ano de Nasimento: '))
anoA = date.today().year
idade = anoA - anoN
idadeF = 18 - idade
idadeP = idade - 18
print('A sua idade atual é de {} anos no ano de {}.'.format(idade, anoA))
if idade < 18:
    ano = anoN + 18
    print('Você ainda não esta na idade de alistamento, ainda faltam {} anos'.format(idadeF))
    print('Você deverá se alistar no ano de {}'.format(ano))
elif idade == 18:
    print('Você está na idade de alistamento, Compareça \033[31mIMEDIATAMENTE\033[m a um posto de alistamento')
elif idade > 18:
    anoV = anoN + 18
    print('E se passaram {} anos para o seu alistamento'.format(idadeP))
    print('Você deveria ter se alistado no ano de {}'.format(anoV))