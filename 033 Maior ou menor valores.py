# Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('primeiro numero: '))
n2 = int(input('segundo numero: '))
n3 = int(input('terceironumero: '))
# Verificando o numero menor
menor = n1 # considerando que o n1 seja o menor
if  n2<n1 and n2<n3:
    menor = n2
if  n3<n2 and n3<n1:
    menor = n3
print('O Menor numero digitado é {}'.format(menor))
# Verificando quem é o maior
maior = n1 # considerando que o n1 seja o maior
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('o Maior numero digitado é {} '.format(maior))



