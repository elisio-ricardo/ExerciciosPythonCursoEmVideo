nome = str(input('Digite o seu nome completo: ')).strip()  # retira os espaços da frente e de trás
print(f'O seu nome em letras maiusculas é: {nome.upper()}')  # deixa as letras em maiuscula
print(f'O seu nome em letras minusculas é: {nome.lower()}')  # deixa as letras em minusculas
print(f'O total de letras no seu nome é {len(nome) - nome.count(" ")}')  # conta todos os caracteres e subtrai os espaços
print(f'O primeiro nome tem {len(nome.split()[0])} letras')  # numera os caracteres a partir dos espaços, assim pode
# selecionar a palavra desejada
