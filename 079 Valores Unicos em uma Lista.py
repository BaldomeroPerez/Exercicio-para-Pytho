#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numeros = list()
while True:
    n = int(input('Digite um Valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor Adicionado com sucesso ...')
    else:
        print('Numero Duplicado! Não vou Adicionar ...')
    r = str(input('Voce quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-='* 30)
numeros.sort()
print(f'Voce digitou os valores:{numeros}')

