# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor

n = int(input('digite um numero: '))
a = n - 1
s = n + 1
print('analisando o numero {} o seu antecessor é: {} e seu sucessor é: {}'.format( n, a, s))

# ou de outra maneira
n = int(input('digite um numero: '))
#print('analisando o numero {} o seu antecessor é: {} e seu sucessor é: {}'.format( n, (n-1),(n+1)))

print(f'Analisando o numero {n}, o seu sucessor é {n-1} e seu antecessor é {n+1}.') # versão mais moderna