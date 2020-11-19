#Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.

times = ('Corinthians', 'Palmeiras', 'São Paulo', 'Santos', 'Gremio', 'Cruzeiro', 'Flamengo'
         'Vasco', 'Chapecoense', 'Atletico', 'Botafogo', 'Atletico-PR', 'Bahia', 'Fluminense',
         'Sport', 'Vitoria', 'Coritiba', 'Avai', 'Ponte Preta', 'Atletico-GO')
print('-=' * 15)
print(f'Lista de Times {times}')
print('-=' * 15)
print(f'Os cinco primeiros são: {times[0:5]}')
print('-=' * 15)
print(f'Os ultimos quatro colocados são: {times[-4:]}')
print('-=' *15)
print(f'Os times em ordem alfabetica:{sorted(times)}') # coloca em ordem alfametica mas não muda tupla
print('-=' * 15)
print(f' O Chapecoense está na {times.index("Chapecoense") + 1}ª posição')






