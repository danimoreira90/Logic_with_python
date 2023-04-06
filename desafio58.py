num=int(input('Insira um número inteiro: '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot = tot + 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi dividido {} vezes'.format(num, tot))
if tot == 2:
    print('Ele é um número primo')
else:
    print('Ele não é um número primo')






