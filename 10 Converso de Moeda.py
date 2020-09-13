# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('Quanto você tem na carteira?: R$'))
dolar = real / 4.50
print('Com R$ {:.2f} voce pode comprar Us$ {:.2f}'.format(real,dolar))
