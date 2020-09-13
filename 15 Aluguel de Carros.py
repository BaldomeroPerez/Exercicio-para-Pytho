# Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = int(input('Quantos dias ficou alugado: '))
km = float(input('Quantos kilometros rodou: '))
pgdias = dias * 60
pgkm = km * 0.15
print('O valor total de dias a pagar é R$ {:.2f}'.format(pgdias))
print('O valor total da kilometragem  a pagar é R$ {:.2f}'.format(pgkm))
final = pgdias + pgkm
print('O Valor total a pagar dos dias e kilometragem é R$ {}'.format(final))


# ou simplificado

dias = int(input('Quantos dias ficou alugado: '))
km = float(input('Quantos kilometros rodou: '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R$ {:.2f}'.format(pago))
