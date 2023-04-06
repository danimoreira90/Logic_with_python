lista = []
pessoas = {}
totidade = 0
mulheres = {}
listamulheres = []
while True:
    pessoas['Nome'] = str(input('Nome: '))
    pessoas['Sexo'] = str(input('Sexo: [M/F]: ')).strip().upper()[0]
    if pessoas['Sexo'] == 'F':
        mulheres['Nome'] = pessoas['Nome']
        listamulheres.append(mulheres.copy())
    pessoas['Idade'] = int(input('Idade: '))

    lista.append(pessoas.copy())
    totidade += pessoas['Idade']
    flag = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if flag == 'N':
        break
print('-='*35)
print(f' - O grupo tem no total {len(lista)} pessoas.')
media = (totidade)/(len(lista))
print(f' - A média de idade do grupo é de {media} anos.')
#print(lista)
#print(listamulheres)
print(' - As mulheres cadastradas foram: ', end=' ')
for m in range(0, (len(listamulheres))):
    print(listamulheres[m]["Nome"], end=' ')
print()
print(f' - Lista de pessoas com idade acima da média: ')
pma = {}
listapma = []
for i, v in enumerate(lista):
    if lista[i]["Idade"] > media:
        pma['Nome'] = (lista[i]["Nome"])
        pma['Sexo'] = (lista[i]["Sexo"])
        pma['Idade'] = (lista[i]["Idade"])
        listapma.append(pma.copy())
#print(listapma)
for i, v in enumerate(listapma):
    print(f'Nome: {listapma[i]["Nome"]}; Sexo: {listapma[i]["Sexo"]}; Idade: {listapma[i]["Idade"]}.')
print('<<<<< ENCERRANDO PROGRAMA >>>>>')