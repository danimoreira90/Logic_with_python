from random import randint
from time import sleep
from operator import itemgetter

jogadores = {}
jogadores['Jogador1'] = randint(1,6)
jogadores['Jogador2'] = randint(1,6)
jogadores['Jogador3'] = randint(1,6)
jogadores['Jogador4'] = randint(1,6)
Ranking = []
Ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('     VALORES SORTEADOS')
for keys, values in jogadores.items():
    print(f'O {keys} tirou o número {values}.')
    sleep(1)
print('=-'*20)
print('    Ranking dos jogadores ')
for pos, v in enumerate(Ranking):
    print(f'{pos+1}º Lugar ==> {v[0]} com {v[1]}.')

