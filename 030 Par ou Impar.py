# Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
numero = int(input('Me diga um numero qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('o numero {} é par'.format(numero))

else:
    print('o numero {} é impar'.format(numero))


# print('resultado foi {} '.format(resultado))
