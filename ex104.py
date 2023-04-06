def notas(*n, sit=False):
    """
    --> Função que calcula a média e situação de diversos alunos devolvendo um dicionário.
    :param n: Uma ou mais notas dos alunos.
    :param sit: Situação mediante a média das notas inseridas.
    :return: Dicionário com informações sobre as notas e situação da turma.
    """
    r = {}
    r['Total'] = len(n)
    r['Maior Nota'] = max(n)
    r['Menor Nota'] = min(n)
    r['Média das Notas'] = sum(n)/len(n)
    if sit:
        if r['Média das Notas'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Média das Notas'] >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'

    return r


resp = notas(7.5, 3.9, 4.7, 9.8, sit=True)
print(resp)
help(notas)