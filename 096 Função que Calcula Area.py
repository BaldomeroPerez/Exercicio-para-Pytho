#Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(larg, comp):
    a = larg * comp
    print(f'A area do terreno {larg} X {comp} é de {a}m².')

# PROGRAMA PRINCIPAL
print(' CONTROLE DE TERRENOS')
print('-'*20)
l = float(input('LARGURA (MT): '))
c = float(input('COMPRIMENTO (MT): '))
area(l, c)
