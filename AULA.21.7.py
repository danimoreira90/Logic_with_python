#RETORNO DE VALORES
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s



r1 = somar(5, 6, 3)
r2 = somar(3, 5)
r3 = somar()
r4 = somar(4, 9)
print(f'As somas foram {r1}, {r2}, {r3}, {r4}.')