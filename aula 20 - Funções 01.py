'''def moslin():
    print('='*20)
# programa principal
moslin()
print('   CURSO EM VIDEO   ')
moslin()
print('   APRENDENDO PYTHON   ')
moslin()
print('   MIRO PEREZ   ')
moslin()'''

'''def titulo(txt):
    print('='*30)
    print(txt)
    print('='*30)

# programa principal
titulo('   CURSO EM VIDEO 1   ')
titulo('   APRENDENDO PYTHON 2  ')
titulo('   MIRO PEREZ 3  ')'''


'''a=4
b=5
s=(a + b)
print(s)

a = 8
b = 9
s = (a + b)
print(s)

a = 1
b = 2
s = (a + b)
print(s)
print('')
def soma(a,b):
    print(f'A={a} e B{b}')
    s =  a + b
    print(f'A soma de A + B = {s}')


#PROGRAMA PRINCIPAL
soma (b=4,a=5)
soma (8,9)
soma (2,1)'''


'''def contador(*num):
    tam = len(num)
    #print(num)
    print(f'Recebi os valores {num} e são todos os {tam} numeros')


contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)'''


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6,3,9,1,0,2]
dobra(valores)
print(valores)


def soma (*valores):
    s =  0
    for num in valores:
        s += num
    print(f'Somando os valores{valores} temos {s} ')

soma(5,5)
soma(2,9,9)


