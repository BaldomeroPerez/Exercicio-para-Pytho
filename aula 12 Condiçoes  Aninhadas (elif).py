nome = str(input("Qual é o seu nome: "))
if nome == "Miro":
    print('Que nome bonito')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Jose':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana, Claudia, Jessica, Juliana':
    print('Nome feminino')
else:
    print('Seu nome é bem comun')
print('Tenha um bom dia {}!'.format(nome))

