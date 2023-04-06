a=float(input('insira o comprimento da reta a: '))
b=float(input('insira o comprimento da reta b: '))
c=float(input('insira o comprimento da reta c: '))
if (b-c)<a and (b+c)>a and (a-c)<b and (a+c)>b and (a-b)<c and (a+b)>c:
    print('é possível formar um triângulo')
if a > b + c or b > c + a or c > a + b:
    print('Não é possível formar um triângulo')
elif a == b == c:
    print('Esse triângulo é EQUILÁTERO')
elif a == b !=c or a == c !=b or b == c != a:
    print('Esse triângulo é ISOSCELES')
elif a !=b != c:
    print('Esse triângulo é ESCALENO')
