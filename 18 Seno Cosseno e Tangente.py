# Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo = float(input('Digite o angulo que voce deseja: '))
seno = math.sin(math.radians(angulo))
print('O angulo de {} tem o seno de {:.2f}'.format(angulo,seno))
cosseno = math.cos((math.radians((angulo))))
print('O angulo de {} tem o cosseno de {:.2f}'.format(angulo,cosseno))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem a tangente de {:.2f}'.format(angulo,tangente))

# ou simplificando
from math import radians,sin,cos,tan
angulo = float(input('Digite o angulo que voce deseja: '))
seno = sin(radians(angulo))
print('O angulo de {} tem o seno de {:.2f}'.format(angulo,seno))
cosseno = cos((radians((angulo))))
print('O angulo de {} tem o cosseno de {:.2f}'.format(angulo,cosseno))
tangente = tan(radians(angulo))
print('O angulo de {} tem a tangente de {:.2f}'.format(angulo,tangente))
