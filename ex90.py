alunos = {}
alunos['Nome'] = str(input('Nome: '))
alunos['Média'] = float(input('Média: '))
print(f'Nome é igual a {alunos["Nome"]}.')
print(f'Média é igual a {alunos["Média"]} ')

if alunos['Média'] >= 7:
    print('Situação: APROVADO')
else:
    print('situação: REPROVADO')