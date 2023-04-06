pessoas = []
dados = []
maispes = maislev = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso em Kg: ')))
    if len(pessoas) == 0:
        maispes = maislev = dados[1]
    else:
        if dados[1] > maispes:
            maispes = dados[1]
        if dados[1] < maislev:
            maislev = dados[1]
    pessoas.append(dados[:])
    dados.clear()

    flag = str(input('Deseja continuar [S/N]: ')).strip().upper()
    while flag not in 'SN':
        flag = str(input('Opção inválida. Deseja continuar [S/N]: ')).strip().upper()
    if flag == 'S':

        continue
    if flag == 'N':
        break
print('=-' *40)
print(f'Você cadastrou ao todo {len(pessoas)} pessoas.')
print(f'O maior peso cadastrado foi de {maispes}kg. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == maispes:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso cadastrado foi de {maislev}kg. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == maislev:
        print(f'[{p[0]}] ', end='')
print()

