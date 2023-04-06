from random import randint
print('=-=-'*20)
print('{:^60}'.format('GERADOR DE NÚMEROS'))
print('=-=-'*20)
tupla = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
tuplasorted = sorted(tupla)
print(f'Os números gerados foram: {tupla}')
print(f'O maior número gerado foi {tuplasorted[0]} e o menor número foi {tuplasorted[4]}')



