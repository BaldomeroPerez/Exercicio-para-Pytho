# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços)

nome = str(input('Digite seu Nome completo: ')).strip()
print('Analisando o seu nome ')
print('seu nome em Maiusculas é : {}'.format(nome.upper()))
print('seu nome em minuscula é : {}'.format(nome.lower()))
print('seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('seu primeiro nome tem {} letras'.format(nome.find(' ')))

# ou simplificando
separa = nome.split()
print('seu primeiro nome é {} e ele tem {} letras'.format(separa(0),len(separa[0])))


# strip() remove espaços inuteis no inicio e fim.
# upper() troca as letras para minusculas para maisculas.
# lower() troca as letras maisculas para minusculas.
# len() mostra comprimento da frase com espaços no meio.
# count(0) = conta 0s espaços em branco entre as palavras das frase.
# find(0) encontra o começo da frase.