d=float(input('Insira a distância da viagem em km: '))
if d <=200:
    print('O valor de sua passagem é {}'.format((d*0.5)))
else:
    print('O valor de sua passagem é {}'.format((d*0.45)))