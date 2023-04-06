import random
import time
print('__'*30)
print('{:^50}'.format('JOGO DA MEGA SENA'))
print('__'*30)
lista = []
jogos = []
quant = int(input('Quantos jogos a serem sorteados? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = random.randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*3, f' SORTEANDO {quant} JOGOS', '-=' *3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    time.sleep(1)
print('-=' *5, '<< BONS JOGOS!! >>', '-=' *5)



