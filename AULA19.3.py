estado = {}
brasil = []
for c in range(0,3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for estado in brasil:
    for keys, values in estado.items():
        print(f'O campo {keys} tem valor {values}.')
    print('-='*10)
    

