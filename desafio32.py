n1=float(input('Insira o primeiro número: '))
n2=float(input('Insira o segundo número: '))
n3=float(input('Insira o terceiro número: '))
#MENORES
if n1 < n2 and n1 < n3 :
    print('n1 é o menor valor')
if n2 < n1 and n2 < n3:
    print('n2 é o menor valor')
if n3 < n1 and n3 < n2:
    print('n3 é o menor valor')
#MAIORES
if n1 > n2 and n1 > n3:
    print('n1 é o maior valor')
if n2 > n1 and n2 > n3:
    print('n2 é o maior valor')
if n3 > n2 and n3 > n1:
    print('n3 é o maior valor')
