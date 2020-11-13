from datetime import date
totma = 0
totme = 0
anoA = date.today().year
for c in range(1, 8):
    anoN = int(input(f'Digite o ano de nascimento da {c}° pessoa: '))
    if anoA - anoN > 18:
        totma += 1
    else:
        totme += 1

print(f'Existe {totma} pessoas maiores de idade!')
print(f'Existe {totme} pessoas menores de idade!')
