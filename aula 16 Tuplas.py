'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
# Tuplas são IMUTAVEIS
lanche [1] = 'Salgadinho'
print(lanche[1:3]) # ordem de traz para frente [-3]'''

'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita') # inclui batata frita

for cont in range(0, len(lanche)): # mesma maneira que a de baixo escrito diferente
    print(f'Eu Vou comer {lanche[cont]}')

for comida in lanche:  # mesma maneira que a de cima
    print(f'Eu vou comer {comida}')

for pos, comida in enumerate (lanche): # dua variaveis (pos, comida)
    print(f'Eu vou comer {comida} na posição {pos}') # mostrando posição


    print(len(lanche)) # mudei o identação Ver efeito
print("Comi pra Caramba")

print(sorted(lanche)) # Ordenado Alfabetica'''

a = (2,5,4)
b = (5,8,1,2)
c = a + b # a ordem influencia b + a
print(c)

