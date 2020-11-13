from time import sleep

def maior(*num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando numeros')
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.2)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print()
    print(f'Foram imformados {cont} valores')
    print(f'O maior valor é {maior}')


maior(2, 5, 9, 7, 5, 6, 3, 4)
maior(6, 7, 5, 1, 8, 5)
maior(7, 5, 6)
maior(9)
maior()
