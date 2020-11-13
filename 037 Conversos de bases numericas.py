# Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Digiten um numero inteiro: '))
print('''Escolha uma das bases para conversão;
 [ 1] Converter para Binario
 [ 2] Converter para Octal
 [ 3] Converter para Hexadecimal''')
opção = int(input('Sua Opção: '))
if opção == 1:
    print('{} converti do para Binario é igual a {} '.format(num, bin(num)[2:])) # [2:] é para eliminar os 2 primeiros n da resposta
elif opção == 2:
    print('{} convertido para Octal é igual a {} '.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida. Tente novamente')



