n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))
tupla = (n1, n2, n3, n4)
print(f'Os números inseridos foram {tupla}.')

if n1 or n2 or n3 or n4 == 9:
    print(f'O número 9 foi digitado {tupla.count(9)} vezes.')

if n1 or n2 or n3 or n4 == 3:
    if 3 in tupla:
        print(f'O número 3 está na {tupla.index(3)+1} posição.')
    else:
        print(f'O número 3 não foi digitado.')
print(f'Os valores pares digitados foram', end='')
for c in tupla:
    if c % 2 == 0:
        print(c, end=' ')



