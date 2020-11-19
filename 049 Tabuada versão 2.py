# Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
num = int(input('digite um numero para ver a taboada: '))
for c in range (1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))

#print('{} x {:2} é = {}'.format(num, 1, num*1))
#print('{} x {:2} é = {}'.format(num, 2, num*2))
#print('{} x {:2} é = {}'.format(num, 3, num*3))
#print('{} x {:2} é = {}'.format(num, 4, num*4))
#print('{} x {:2} é = {}'.format(num, 5, num*5))
#print('{} x {:2} é = {}'.format(num, 6, num*6))
#print('{} x {:2} é = {}'.format(num, 7, num*7))
#print('{} x {:2} é = {}'.format(num, 8, num*8))
#print('{} x {:2} é = {}'.format(num, 9, num*9))
#print('{} x {:2} é = {}'.format(num, 10, num*10))
