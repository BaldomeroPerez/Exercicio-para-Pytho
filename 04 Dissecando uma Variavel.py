# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.


a = input('digite algo: ')
print('o tipo primitivo desse valor é: ', type(a))
print('só tem espaços ? ', a.isspace())
print('é um numero ?', a.isnumeric())
print('é alfabético ?', a.isalpha())
print('é alfanumerico ?',a.isalnum())
print('é maiuscula ?', a.isupper())
print('é minuscula ? ', a.islower())
print('palavra capitalizada ?',a.istitle()) # titulo Maiuscula e minuscula