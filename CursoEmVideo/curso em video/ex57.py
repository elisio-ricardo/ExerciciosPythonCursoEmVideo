sexo = str(input('informe o seu sexo: [M/F] ')).strip().upper()
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor, informe o sexo correto: ')).strip().upper()
print('Sexo {} registrado com sucesso'.format(sexo))
