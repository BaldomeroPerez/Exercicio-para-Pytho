# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
def notas(*n, sit=False):
    """
    => Função para analisar notas e situação de varios Alunos
    :param n: Uma ou mais notas do aluno ( aceita varias)
    :param sit: Valor opcional indicando se deve ou não adicionar a situação
    :return: Dicionario com varias informações sobre a situação da turma
    """
    r = dict()
    r['Total']= len(n)
    r['Maior']= max(n)
    r['Menor']= min(n)
    r['Media']= sum(n)/len(n)  # sum = somatoria
    if sit:
        if r['Media'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Media'] >=5:
            r['Situação'] = 'RAZOAVEL'
        else:
            r['Situação'] = 'RUIM'
    return r

# Prog.Principal
resp = notas( 9, 8, 5.5, 5.5, 6.5, sit=True) # SEM O SIT= NÃO APARECE A SITUAÇÃO
print(resp)
#help(notas)