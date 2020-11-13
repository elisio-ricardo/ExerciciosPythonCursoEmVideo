while True:
    num = int(input('Qual tabuada voce gostaria de fazer: '))
    if num < 0:
        break
    for c in range(1, 11):
        print(f' {num} x {c} = {c * num}')
print('Finalizando o Programa')