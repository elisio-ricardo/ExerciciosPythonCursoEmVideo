valor = float(input('Ola Sr. Qual seria o valor do imovel escolhido ? R$  '))
salario = float(input('O valor do seu salario por favor. R$ '))
anos = int(input('Em quantos anos o Sr. deseja pagar o imovel ? '))
mensal = valor / (anos * 12)
print('Para pagar uma casa do valor de \033[31mR${:.2f}\033[m no tempo de \033[31m{}\033[m anos.'.format(valor, anos), end='')
print('A prestação tera um valor de \033[31mR${:.2f}\033[m'.format(mensal))
if mensal < (salario * 30 / 100):
    print('O seu emprestimo foi aprovado, \033[32mPARABENS\033[m pelo imovel')
else:
    print('O seu emprestimo foi \033[31mNEGADO\033[m, escolha um imovel com um valor menor ! ') 