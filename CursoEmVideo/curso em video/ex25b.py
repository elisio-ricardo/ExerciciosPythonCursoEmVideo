def lin():
    print('~-' * 30)


nome = str(input('Digite o seu nome: ')).strip().upper()
while True:
    if 'SILVA' not in nome:
        nome = str(input('Digite o seu nome: ')).strip().upper()
    else:
        break


lin()
print(f'O nome tem silva? \n{"SILVA" in nome}')
lin()
