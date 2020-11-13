def spa():
    print('~-' * 30)
def cor():
    print('\033[m')


nome = str(input("Digite o seu nome completo: ")).strip()
spa()
print(f'Muito prazer em te conhecer')
spa()
print(f'O seu primeiro nome é {nome.split()[0]}')
spa()
print(f'E o seu ultimo nome é {nome.split()[-1]}')
spa()

