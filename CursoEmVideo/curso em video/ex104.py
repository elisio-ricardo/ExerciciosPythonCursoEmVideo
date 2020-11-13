def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;33mERRO! Digite um valor valido.\033[m')
        if ok:
            break
    return valor


n = leiaint('Digite um numero: ')
print(f'Você acabou de digitar o numero {n}')
