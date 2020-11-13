from datetime import date
anoN = int(input('Digite o ano do seu nascimento: '))
anoA = date.today().year
idade = anoA - anoN
if idade <= 9:
    print('\033[31mClassificação: MIRIM')
elif idade <= 14:
    print('\033[31mClassificação: INFANTIL')
elif idade <= 19:
    print('\033[31mClassificação: JUNIOR')
elif idade <= 25:
    print('\033[31mClassificação: SÊNIOR')
else:
    print('\033[31mClassificação: MASTER')