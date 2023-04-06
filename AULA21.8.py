def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}.')

f1 = fatorial(5)
f2 = fatorial(9)
f3 = fatorial(6)
f4 = fatorial(3)
print(f'Os resultados dos fatoriais acima são: {f1}, {f2}, {f3}, {f4}.')