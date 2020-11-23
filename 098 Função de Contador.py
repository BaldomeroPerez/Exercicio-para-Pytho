#Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c) uma contagem personalizada

from time import sleep


def contador(i, f, p):    # i=inicio f=fim e p=passo
    if p < 0:
        p *= -1    # para eleinar problema de o passo ser negativo
    if p == 0:
        p = 1

    print('='*30)
    print(f'Contagem de {i} ate {f} em {p} a {p}')
    sleep(2)

    if p < 0:
        p *= -1    # para eleinar problema de o passo ser negativo
    if p == 0:
        p = 1

    if i < f:   # para eliminar problema de inincio maior que o fim
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print(' FIM ')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('  Fim  ')


#Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('='*30)
print('Agora é a sua vez de personalizar a contagem ')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)

