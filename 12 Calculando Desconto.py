# Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
preço =  float(input('Qual é o preço do Produto: R$ '))
novo = preço - (preço * 5/100)
print('O produto que custava R$ {:.2f} agora na promoção, com desconto de 5% custa R$ {:.2f}'.format(preço, novo))
