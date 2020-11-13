from random import choice
from time import sleep
print('#' * 30)
print('      Sorteio de Alunos')
print('#' * 30)
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('-=' * 30)
sleep(1)
print(' O aluno escolhido foi  \033[31m{}\033[m'.format(escolhido))
print('-=' * 30)
