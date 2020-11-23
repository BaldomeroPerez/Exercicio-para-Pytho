'''num =[2,5,9,1]
num[2] = 3
num.append(7)
num.insert(2, 2) # vai inserir na posição 2 o numero 0
if 4 in num:    # elimina o 4 para não dar erro
    num.remove(4)
else:
   print('Nao achei o numero 4')
num.pop(4)  # sem informação elimina o ultimo da lista
num.remove(2) # revome o primeiro numero 2 da lista sem continuar
print(num)
print(f'Essa lista {len(num)} elementos')'''


'''valores = []
valores.append(5)
valores.append(9)
valores.append(4)
#for v in valores:
# print(f'{v}...', end=' ')
for c, v in enumerate(valores):
    print(f' Na posição {c} encontrei o valor {v}!')'''

'''valor = list()
for cont in range(0, 5):
    valor.append(int(input('Digite um valor: ')))
for c, v in enumerate(valor):
    print(f' Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')'''


'''a = [2,3,4,7]
b = a  # assim ele faz ligação entre A e B
b [2] = 8
print(f'Lista A:{a}')
print(f'Lista B:{b}')'''

a = [2,3,4,7]
b = a[:]    # copia dos valores de A em B
b [2] = 8
print(f'Lista A:{a}')
print(f'Lista B:{b}')
