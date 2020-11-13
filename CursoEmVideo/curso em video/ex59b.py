num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
opçao = 0
while opçao != 5:
    print('=~' * 30)
    print(""" Escolha uma das opções
     [1] Somar
     [2] Multiplicar
     [3] Maior
     [4] Novos numeros
     [5] Sair do programa """)
    print('=~' * 30)
    opçao = int(input(' Opção: '))
    print('^^' * 30)
    if opçao == 1:
        print(f' A soma dos valores {num1} e {num2} é igual a {num1 + num2}')
    elif opçao == 2:
        print(f' A multiplicação dos valores {num1} x {num2} é igual a {num1 * num2}')
    elif opçao == 3:
        if num1 > num2:
             print(f'O maior valor entre {num1} e { num2} é {num1}')
        else:
             print(f'O maior valor entre {num1} e {num2} é {num2}')
    elif opçao == 4:
        print('Digite novos Valores')
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
    elif opçao == 5:
        print('Finalizando')
    else:
        print('DIGITE UMA OPÇÃO VALIDA')
print('Fim Do Programa!')