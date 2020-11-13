num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para a conversão:
[ 1 ] converter para BINARIO 
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opçao = int(input('Sua opção: '))
if opçao == 1:
    print('{} convertido para BINARIO é igual a {}'.format(num, bin(num)[2:])) # O [2:] é para nao usar as 2 primeiras letras do codigo que vai aparecer
elif opçao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opçao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida. TENTE NOVAMENTE')