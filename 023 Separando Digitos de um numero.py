# Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
num = int(input('informe um numero:'))
n = str(num)
print('analisando o numero {} '.format(num))
print('a unidade: {} '.format(n[3]))
print('a dezena: {} '.format(n[2]))
print('a centena: {} '.format(n[1]))
print('a milhar: {} '.format(n[0]))

# se colocar - milhar não funciona (da erro)
# ou

num = int(input('informe um numero:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num //1000 % 10
print('analisando o numero {} '.format(num))
print('a unidade: {} '.format(u))
print('a dezena: {} '.format(d))
print('a centena: {} '.format(c))
print('a milhar: {} '.format(m))



