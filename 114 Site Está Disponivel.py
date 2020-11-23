import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except: # urllib.erro.URLError:
    print('O Site PUDIM não está acessivel no momento')
else:
    print('Consegui acessar o site Pudim com sucesso')

    print(site.read()) # da o codigo do site inteiro.