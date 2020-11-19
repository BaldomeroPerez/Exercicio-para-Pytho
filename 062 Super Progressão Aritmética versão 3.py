# Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
print('Gerador de P.A.')
print('=_=' * 12)
primeiro = int(input('Primeiro termo: '))
razao =  int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end=' ')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos Você quer mostrar a mais? '))
print('Progressão Finalizada com {} termos mostrados.'.format(total))


