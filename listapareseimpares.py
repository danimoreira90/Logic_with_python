listatotal = []
listapares = []
listaimpares = []
while True:
    n = int(input('Digite um valor:'))
    listatotal.append(n)
    if n % 2 == 0:
        listapares.append(n)
    if n % 2 == 1:
        listaimpares.append(n)
    flag = str(input('Quer continuar [S/N]: ')).strip().upper()
    while flag not in 'SN':
        flag = str(input('Opção inválida. Quer continuar [S/N]: ')).strip().upper()
    if flag == 'S':
        continue
    if flag == 'N':
        break
print(f'A lista com todos os valores é {listatotal}.')
print(f'A lista com os valores pares é {listapares}.')
print(f'A lista com os valores ímpares é {listaimpares}.')
