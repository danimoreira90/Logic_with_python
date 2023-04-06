v=float(input('Qual é o valor da casa em R$? '))
s=float(input('Qual é o salário do comprador em R$?  '))
a=float(input('Em quantos anos será paga a casa? '))
if v/(a*12) < (s*30)/100:
    print('Seu empréstimo foi aprovado')
else:
    print('Seu empréstimo foi recusado')

