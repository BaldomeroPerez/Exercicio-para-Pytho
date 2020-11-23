#help(input)
#print(input.__doc__)

def contador(i, f, p):
    """
    Faz a contagem e mostra na tela
    :param i: Inicio da Contagem
    :param f: Fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('Fim')

contador(0, 100, 10)
help(contador)

print('--=--'* 10)

def somar(a=0, b=0, c=0):  # colocado =0 para podermos eliminar qualque das variaveis
    """

    :param a: Primeiro valor
    :param b: Segundo Valor
    :param c: Terceiro Valor
    :return: sem retorno
    """
    s=(a + b + c)
    print(f' A soma vale {s}')

somar(3, 2, 5)  # se eliminar o 5 dara erro pois falta o c

print('--='*10)

def função():
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
função()
print(f' N1 fora vale {n1}')

print('--='* 10)


def somar(a=0, b=0, c=0):
    s=(a + b + c)
    #print(f' A soma vale {s}')
    return s

r1 = somar(3, 2, 5)
r2 = somar(2 ,2 )
r3 = somar(6)
print(f' Os resultados foram {r1}, {r2} e {r3}')

print('-='*10)

def fatorial (num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}.')

print('--='*10)

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um numero:'))
if(par(num)):
    print('É Par')
else:
    print('É impar')

print('--='*10)


