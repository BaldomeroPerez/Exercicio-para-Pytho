# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um numero inteiro valido.\33[m')
        if ok:
            break
    return valor


# Prog.Principal
n = leiaint('Digite um numero: ')
print(f' Voce acabou de digitar o numero {n}.')
