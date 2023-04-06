lista = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    flag = str(input('Quer continuar [S/N]:')).strip().upper()
    while flag not in 'SN':
        flag = str(input('Tente novamente. Quer continuar [S/N]:')).strip().upper()
    if flag == 'S':
        continue
    if flag == 'N':
        break
if 5 in lista:
    print(f'O valor 5 foi digitado e está na lista na posição {lista.index(5)}')
else:
    print('O valor 5 não está na lista')
lista.sort(reverse=True)

print(f'Você digitou {len(lista)} valores')
print(f'A lista em ordem decrescente é {lista}')


