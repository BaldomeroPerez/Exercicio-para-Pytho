# Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite um Numero: '))
tot = 0
for c in range(1, num +1):
    if num % c == 0:
        print('\33[33m',end=' ')
        tot +=1
    else:
        print('\33[31m',end=' ')
    print('{} '.format(c), end=' ')

print('\n\33[m O numero {} foi dividido {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele é Primo')
else:
    print('E por isso Não é Primo')
