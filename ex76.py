valores = []
while True:

    v = (int(input('Digite um valor: ')))
    if v not in valores:
        valores.append(v)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado. Não adicionado.')

    flag = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if flag not in 'SN':
        flag = str(input('Opção inválida. Deseja continuar? [S/N]: ')).strip().upper()
    if flag == 'S':
        continue
    if flag == 'N':
        break
print(valores)