# Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
somaidade = 0
mediaidade = 0
maioridadehomen = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('====== {}ª Pessoa ====='.format(p))
    nome = str(input('Nome: ')).strip( )
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '.strip( )))
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomen = idade
        nomevelho = nome
    if sexo in'Mm'and idade > maioridadehomen:
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
         totmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {}'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {} '.format(maioridadehomen, nomevelho))
print('Ao total são {} mulheres com menos de 20 anos'.format(totmulher20))
