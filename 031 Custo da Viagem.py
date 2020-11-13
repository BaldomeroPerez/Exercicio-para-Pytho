# Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
distancia = float(input('Qual a distancia da sua viagem? '))
print('Voce está prestes a começar uma viagem de {} km'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('O preço de sua viagem sera de R$ {:.2f}'.format(preço))

# ou simplificado

distancia = float(input('Qual a distancia da sua viagem? '))
print('Voce está prestes a começar uma viagem de {} km'.format(distancia))
prço = distancia * .50 if distancia <= 200 else distancia * .45
print('O preço de sua viagem sera de R$ {:.2f}'.format(preço))

