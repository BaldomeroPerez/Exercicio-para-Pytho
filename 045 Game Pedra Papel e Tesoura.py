# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
itens = ( 'Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas Opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
print('-=-' * 10)
jogador = int(input('Qual é a sua jogada? '))
print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Po')
print('O computador jogou {}'.format(itens[computador]))
#print('O Jogador jogou {}'.format(itens[jogador]))
print('-=-' * 10)
if computador == 0:   # computador jogou Pedra
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador Vence')
    elif jogador == 2:
        print('Computador Vence')
    else:
        print('JOGADA INVALIDA!')
elif computador == 1:   # computador jogou Papel
    if jogador == 0:
        print('Computador Vence ')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador Vence')
    else:
        print('JOGADA INVALIDA!')
elif computador == 2:  # computador jogou Tesoura
    if jogador == 0:
        print('Jogador Vence')
    elif jogador == 1:
        print('Computador Vence')
    elif jogador == 2:
        print('Empate')
    else:
        print('JOGADA INVALIDA!')


#print('o computador escolheu {}'.format(itens[computador]))(linha 4)


