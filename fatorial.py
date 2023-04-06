n = int(input('Insira um valor para calcular seu fatorial: '))
c = n
f = c
print('Calculando {}! ='.format(n), end=' ')
while c > 0:
    print('{}'.format(c), end='')
    print(' x'if c > 1 else ' =', end = ' ')
    f = f*c
    c -= 1
print('{}'.format(f))