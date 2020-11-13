from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Data de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Numero da ctps: [0 não tem] '))
if dados['ctps'] != 0:
    dados['contrataçao'] = int(input('Ano da contratação: '))
    dados['salario'] = float(input('Qual o salario: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contrataçao'] + 35) - datetime.now().year)
print('-=' * 30)
for t, m in dados.items():
    print(f' {t} é {m}')
