# Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1  # ou cont += 1 Contador
        soma = soma + c  # ou soma += c
print('A soma de todos os {} valores solicitados é {} '.format(cont, soma))

        #print(c, end=' ') linha 5
