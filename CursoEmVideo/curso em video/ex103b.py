def ficha(jog='<DESCONHECIDO>', gols=0):
    print(f'O jogador {jog} fez {gols} gol(s) no campeonato')


n = str(input('Nome do jogador: '))
g = str(input('Numero de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
