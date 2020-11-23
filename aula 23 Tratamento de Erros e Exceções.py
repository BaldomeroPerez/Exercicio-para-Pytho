#print(x)
#n=int(input('numero'))
try:
    a=int(input('Numerador:'))
    b=int(input('Denaminador:'))
    r = a / b
#except Exception as erro:
    # print("INFELISMENTE TIVEMOS UM PROBLEMA")
    #print(f'Problema encontrado foi{erro.__class__}')
except (ValueError, TypeError):
    print('Tivemos um problema de tipo de dados que voce digitou')
except ZeroDivisionError:
    print('Nao foi possivel dividir um numero por Zero')
except KeyboardInterrupt:
    print('O usuario preferiu não informar os dados')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.2f}')
finally:
    print('Volte sempre. MUITO OBRIGADO.')

