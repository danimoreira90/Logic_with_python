lista = []
listapares = []
listaimpares = []
for c in range(1,8):
    n = int(input(f'Digite o {c}º valor: '))
    lista.append(n)
for v in lista:
    if v % 2 == 0:
        listapares.append(v)
        listapares.sort()
    if v % 2 == 1:
        listaimpares.append(v)
        listaimpares.sort()
print(f'Os valores pares digitados foram {listapares}.')
print(f'Os valores ímpares digitados foram {listaimpares}')

