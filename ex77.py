valores = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > valores[-1]:
        valores.append(n)
        print('Valor adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos += 1
print('=-'*30)
print(f'Os valores adicionados em ordem foram {valores}.')

