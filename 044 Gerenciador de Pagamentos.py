## Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
print('{:=^40}'.format(' MIROS BOUTIQUE '))
preço = float(input('Preços das Compras: R$ '))
print('''FORMA DE PAGAMENTO
[ 1 ] A VISTA em Dinheiro ou Cheque
[ 2 ] A VISTA no Cartão
[ 3 ] 2x no CARTÃO
[ 4 ] 3x  ou Mais no CARTÃO''')
opção = float(input('Qual é a opção?: '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5/ 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Suas compras serão parceladas em 2x de {:.2f} sem juros'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 /100)
    totparc = int(input('Quantas Parcelas?: '))
    parcela = total / totparc
    print('Suas compras serão parceladas em {:.2f}x de R$ {:.2f} com juros'.format(totparc,parcela))
else:
    total = preço
    print('Opção invalida de Pagameto. Tente novamete!')
print('Suas compras de R$ {:.2f} vão custar R$ {:.2f} no final!.'.format(preço,total))




