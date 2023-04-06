i=int(input('Insira sua idade: '))
if i < 18:
    print('Você ainda irá se alistar. Falta {} anos'.format(18-i))
elif i == 18:
    print('É o momento de ir se alistar.')
elif i > 18:
    print('Já passou da data de alistamento. Passaram {} anos.'.format(i-18))