# Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que
from datetime import date
atual = date.today().year
nasc = int(input('Ano de Nascimento: '))
idade =  atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Voce deve se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo =  18 - idade
    print('Voce ainda não tem 18 anos. Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Voce já deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('Voce deveria ter se alistado em {} '.format(ano))

