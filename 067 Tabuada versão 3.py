#Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
while True:
    n = int(input('Quer ver a taboada de qual valor?: '))
    if n < 0:
        break
    print('_' * 20)
    for c in range (1, 11):
        print(f'{n} x {c} é = {n*c}')
    print('_' * 20)
print('PROGRAMA DA TABUADA ENCERRADO. VOLTE SEMPRE')


# ANTERIOR
'''for c in range (1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))'''
