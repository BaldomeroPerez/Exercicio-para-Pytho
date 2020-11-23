#Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um numero inteiro valido.\033[m')
            continue
        except (KeyboardInterrupt): # não funciona para o pycharm 2019
            print('\n\033[31m Usuario preferiu não digitar esse numero\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um numero inteiro valido.\033[m')
            continue
        except (KeyboardInterrupt): # nao funciona para pycharm 2019
            print('\n\033[31m Usuario preferiu não digitar esse numero\033[m')
            return 0
        else:
            return n


n1 =  leiaInt('Digite um inteiro: ')
n2 =  leiaFloat('Digite um Real: ')

print(f'O valor inteiro digitado foi: {n1} e o real foi {n2}.')
