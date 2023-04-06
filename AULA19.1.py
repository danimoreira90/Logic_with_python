pessoas = {'nome': 'Daniel', 'Sexo': 'M', 'Idade': '32'}
pessoas['Peso'] = 100.5
print(f'O {pessoas["nome"]}, tem {pessoas["Idade"]} anos e pesa {pessoas["Peso"]}kg.')
print(pessoas.items())
print(pessoas.values())
print(pessoas.keys())
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('=-='*10)
for k in pessoas.values():
    print(k)
print('=-='*10)
for k in pessoas.keys():
    print(k)