import datetime
ano=int(input('Insira o ano a analisar, Insira 0 para analisar o ano atual'))
if ano ==0:
    print('O ano inserido é {}'.format(datetime.date.today().year))
if ano % 4==0 and ano % 100 !=0 or ano % 400 ==0:
    print('O ano inserido é bissexto')
else:
    print('O ano inserido não é bissexto')
