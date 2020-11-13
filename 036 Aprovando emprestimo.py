# Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Qual é o valor da casa? R$ '))
salario = float(input('Qual é o seu salario atual? R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa /(anos * 12) # valor da casa em prestaçoes mesais
minimo = (salario * 30/100) # maximo de 30% sobre o salario para parcela
print('Para financiamento da casa de R$ {:.2f} em {} anos as parcelas serão de R$ {:.2f}'.format(casa,anos,prestação))
if prestação <= minimo:
    print('Emprestimo PODE ser consedido! ')
else:
    print('Emprestimo NEGADO!')