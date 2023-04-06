n1=float(input('Insira a primeira nota:  '))
n2=float(input('Insira a segunda nota: '))
m=(n1+n2)/2
if m < 5.0:
    print('\033[0;34mREPROVADO\033[m')
elif m >= 5.0 and m < 6.9:
    print('\033[0;34mRECUPERAÇÃO\033[m')
elif m >= 7.0:
    print('\033[0;34mAPROVADO\033[m')