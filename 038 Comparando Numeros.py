# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
n1 =int(input('Primeiro numero: '))
n2 =int(input('Segundo numero: '))
if n1 > n2:
    print('O PRIMEIRO numero é maior')
elif n2 > n1:
    print('O Segundo numero é maior: ')
elif n1 == n2:   # pode ser substituido por else:
    print('Os dois numeros são IGUAIS')

# ou
else:
    print('Os dois numeros são IGUAIS')
