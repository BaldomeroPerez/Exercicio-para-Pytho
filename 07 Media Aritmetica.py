# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('digite um numero: '))
d = n * 2
t = n * 3
r = n **(1/2)
print('o dobro de {} é: {}'.format(n,d))
print('o triplo de {} é: {}'.format(n,t))
print('a raiz quadrada de {} é: {:.2f} '.format(n,r))

# outra maneira
n = int(input('digite um numero: '))
print('o dobro de {} é: {}'.format(n,(n*2)))
print('o triplo de {} é: {}'.format(n,(n*3)))
print('a raiz quadrada de {} é: {:.2f} '.format(n,(n**(1/2))))

# outra maneira
n = int(input('digite um numero: '))
print('o dobro de {} é: {}'.format(n,(n*2)))
print('o triplo de {} é: {}'.format(n,(n*3)))
print('a raiz quadrada de {} é: {:.2f} '.format(n,pow(n,(1/2))))

print(f'Analisando o numero {n}, o dobro é {d}, o triplo é {t} e a raiz quadrada é {r:.2f}.')
