valores = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}ºvalor: '))
    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)
print('=-'*30)
valores[0].sort()
valores[1].sort()
print(f'Os valores pares digitados foram {valores[0]}')
print(f'Os valores ímpares digitados foram {valores[1]}')