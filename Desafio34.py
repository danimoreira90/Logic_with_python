s = float(input('Insira seu salário em R$: '))
a1 = ((s * 10) / 100)
a2 = ((s * 15) / 100)
if s > 1250.00:
    print('Seu aumento é de R${}'.format(a1))
if s < 1250.00:
    print('Seu aumento é de R${}'.format(a2))
