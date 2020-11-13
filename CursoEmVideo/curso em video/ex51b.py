primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

an = primeiro + (10 - 1) * razao

for c in range(primeiro, an + razao, razao):
    print(f'{c}', end=' ')
