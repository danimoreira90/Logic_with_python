v=float(input('insira a velocidade: '))
multa=(v-80)*7
if v >80:
    print('você foi multado em {}'.format(multa))
else:
    print('você está abaixo da velocidade limite')
