n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
media=(n1+n2)/2
print('A sua média foi {}'.format(media))
if media>=6:
    print('Você teve uma boa média.')
else:
    print('Você teve uma média ruim.')
