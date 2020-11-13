aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = int(input(f'Media do {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situaçao'] = 'APROVADO'
elif 5 <= aluno['media'] < 7:
    aluno['situaçao'] = 'RECUPERAÇÃO'
else:
    aluno['situaçao'] = 'REPROVADO'
for k, v in aluno.items():
    print(f'{k} é {v}')

