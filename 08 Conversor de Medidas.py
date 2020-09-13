# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input('distancia em metros: '))
cm = medida * 100
mm = medida * 1000

print('a medida {} mt corresponde a {:.0f} centimetros e {:.0f} milimetros'.format(medida,cm,mm))
