def escreva(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)


escreva('Ricardo Canuto')
escreva('Curso em video')
escreva('YoU')
nome = str(input('Escreva o seu nome: '))
escreva(nome)
