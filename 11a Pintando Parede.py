# Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('largura da parede: '))
altura = float(input('altura da parede: '))
área = largura * altura
print('Sua parede tem a dimensão de {} x {} tendo a area de {} m2'.format(largura,altura,área))
tinta = área / 2
print('Para pintar essa parede, voce precisa de {} litros de tinta'.format(tinta))
