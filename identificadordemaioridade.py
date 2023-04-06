import datetime

atual = datetime.date.today().year
cont1 = 0
cont2 = 0
for c in range(0, 7):
    ano = int(input('Insira seu ano de nascimento: '))
    idade = atual - ano
    if idade >= 21:
        cont1 = cont1 + 1
    else:
        cont2 = cont2 + 1
print('{} pessoas são maiores e {} menores'.format(cont1, cont2))


