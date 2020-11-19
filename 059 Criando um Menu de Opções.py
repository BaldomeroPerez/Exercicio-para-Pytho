# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
from time import sleep
n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Numeros
    [ 5 ] Sair do Programa''')
    opção = int(input('>>> Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é = {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('A multiplicação entre {} X {} é = {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os Numeros Novamente:')
        n1 = int(input('Primeiro Numero:'))
        n2 = int(input('Segundo Numero: '))
    elif opção == 5:
        print('FINALIZANDO')
    else:
        print('Opção Invalida. Tente outra vez.')
    print('=-='*15)
    sleep(2)
print('Fim do Programa. Volte Sempre.')


