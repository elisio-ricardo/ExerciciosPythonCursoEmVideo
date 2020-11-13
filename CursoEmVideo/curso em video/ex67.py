while True:
    n = int(input('Digite o valor da tabuada: '))
    print('-'*30)
    print('-'*30)
    if n <= 0:
        break
    for c in range(1, 11):
        print(f'{n} X {c} = {n*c}')
    print('-'*30)
    print('Digite 0 para parar')
    print('-'*30)
print('Programa Tabuada encerrado! ')
