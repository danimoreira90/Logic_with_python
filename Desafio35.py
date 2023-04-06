a=float(input('insira o comprimento da reta a: '))
b=float(input('insira o comprimento da reta b: '))
c=float(input('insira o comprimento da reta c: '))
if (b-c)<a and (b+c)>a and (a-c)<b and (a+c)>b and (a-b)<c and (a+b)>c:
    print('é possível formar um triângulo')
else:
    print('não é possível formar um triângulo')
