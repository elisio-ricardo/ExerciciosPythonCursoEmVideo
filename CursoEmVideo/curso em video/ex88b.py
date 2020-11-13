from random import randint
lista = []
jogos = []
resp = int(input('Quantos jogos você quer jogar: '))
quant = 1
while quant <= resp:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    quant += 1
for i, v in enumerate(jogos):
    print(f'O {i + 1}° jogo foi: {v}')

