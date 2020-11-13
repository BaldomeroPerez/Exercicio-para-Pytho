# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.2f} e {:.2f} a media do aluno é {:.2f}'.format(nota1,nota2,media))
if media >= 5 and media <7:  # ou if 7 > media >= 5
    print(" Aluno em RECUPERAÇÃO")
elif media < 5:
    print("Aluno em REPROVADO")
else:   # ou elif media >= 7:
    print('Aluno APROVADO')



