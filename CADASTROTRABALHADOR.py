from datetime import date
trabalhador = {}
trabalhador['Nome'] = str(input('Nome: '))
trabalhador['Nascimento'] = int(input('Ano de nascimento: '))
trabalhador['CTPS'] = str(input('CTPS (Digite 0 caso não haja registro): '))
idade = date.today().year - trabalhador['Nascimento']

if trabalhador['CTPS'] == 0:
    trabalhador['CTPS'] = ('Não há registro.')
    print(trabalhador)
else:
    trabalhador['Ano de contratação'] = int(input('Insira o ano de contratação: '))
    aposentadoria = trabalhador['Ano de contratação'] + 35
    trabalhador['Salário'] = float(input('Insira o salário em R$: '))
    trabalhador['Idade'] = idade
    trabalhador['Aposentadoria'] = aposentadoria
    print('=-'*15)
    print(trabalhador)
    print('=-'*15)
for keys, values in trabalhador.items():
    print(f'{keys} tem como registro {values}.')

