# Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
frase =str(input('Digite uma frase: ')).upper().strip() #upper= maisculas / strip elimina espaços
palavras = frase.split()
junto = ''.join(palavras)# juntar palavras sem espaços
inverso = ''
for letra in range(len(junto) -1, -1, -1): # fez o inverso da frase
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um Palindromo!')
else:
    print('A frase digitada não é um Palindromo')

#print('Voce digitou a frase: {}'.format(frase))


