# Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
peso = float(input('Quanto voce peso?(KG): '))
altura = float(input('Qual a sua altura?(M): '))
imc = peso / (altura ** 2)
print('O IMC é {:.2f}'.format(imc))
if imc < 18.5:
    print('Voce está ABAIXO do Peso normal!')
elif 18.5 <= imc <25:
    print('Parabens!. Voce está com o Peso IDEAL !')
elif 25 <= imc <30:
    print('Voce está com SOBREPESO!')
elif 30 <= imc < 40:
    print('Voce está OBESO!')
elif imc >= 40:
    print('Cuidado!. Voce está com OBESIDADE MORBIDA! ')
