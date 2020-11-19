# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
from datetime import date
atual =  date.today().year
nascimento = int(input('Data de Nascimento: '))
idade = atual - nascimento
print('o aluno tem {} anos!'.format(idade))
if idade <= 9:
    print('Classifição:  MIRIM')
elif idade > 9 and idade <= 14: # OU <= 14:
    print('Classificação: INFANTIL')
elif idade > 14 and idade <= 19: # OU <= 19:
    print('Classificação: JUNIOR')
elif idade > 19 and idade <= 25: # OU <= 25:
    print('Classificação: SENIOR')
else:
    print('Classificação: MASTER')
