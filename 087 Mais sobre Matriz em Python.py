#Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

matriz =[[0,0,0], [0,0,0], [0,0,0]]
spar = maior = scol = 0
for lin in range(0, 3): # 3 linhas pedindo a matriz preencher a
    for col in range(0, 3):
        matriz [lin][col] = int(input(f'Digite um valor para [{lin}, {col}]: '))
print('-='* 30)
for lin in range(0, 3): # mostrar a matriz na tela
    for col in range(0, 3):
        print(f'[{matriz[lin][col]:^5}]', end='')
        if matriz [lin][col] % 2 == 0:
            spar += matriz[lin][col]
    print()
print('-='* 30)
print(f'A soma dos valores pares é: {spar} ')
for lin in range(0, 3): # for para a linha pois a coluna é 2
    scol += matriz[lin][2] # para somar coluna 3
print(f'A soma da terceira coluna é: {scol} ')
for c in range( 0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O Maior valor da segunda linha é: {maior} ')
