s = 0
for c in range(1, 7):
    n = int(input('Insira um número: '))
    if n % 2 == 0:
        s = s + n
print('O somatório dos valores foi {}'.format(s))
