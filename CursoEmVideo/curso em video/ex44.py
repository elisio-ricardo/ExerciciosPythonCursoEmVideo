preço = float(input('Preço da compra: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro / cheque ( 10 % de desconto )
[ 2 ] À vista cartão ( 5 % de desconto )
[ 3 ] 2x no cartão ( sem desconto )
[ 4 ] 3x ou mais no cartão ( 20 % de juros ) ''')
opção = int(input('Qual é a opção desejada: '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5/100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas: '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = 0
    print('OPCÃO INVALIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final. '.format(preço, total))