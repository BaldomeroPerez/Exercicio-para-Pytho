'''teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) # [:] = copia
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(teste)
print(galera)# lista dentro de outra lista'''

'''galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
print(galera [0])
print(galera[0][1])
print(galera [2][0])
print('='*30) # separando exemplos
for p in galera:
    #print(p[0]) # [0] so os nomes
    print(f'{p[0]} tem {p[1]} anos de idade.')'''

galera = list()
dado = list()
totmai = totmenor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
print('='*30) # separar exemplos

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmenor += 1
print(f'Temos {totmenor} menores e {totmai} maiores de idade.')


