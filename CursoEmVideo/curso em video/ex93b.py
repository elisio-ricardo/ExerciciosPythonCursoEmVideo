lista = {}
partidas = list()
lista['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas o {lista["nome"]} jogou: '))
gols = 0
for c in range(0, tot):
    partidas.append(int(input('Quantos gols na partida: ')))
lista['gols'] = partidas[:]
lista['total'] = sum(partidas)
print('-=' * 30)
print(lista)
print('-=' * 30)
for k, v in lista.items():
    print(f'O campo {k} tem o valor de {v}')
print('-=' * 30)
print(f'O jogador {lista["nome"]} jogou {len(lista["gols"])} partidas')
for i, v in enumerate(lista['gols']):
    print(f'Na partida {i} fez {v} gols')
print(f'Foi um total de {lista["total"]} gols')
