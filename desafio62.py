import random

n = random.randint(0,10)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Insira um valor entre 0 e 10: '))
    palpites += 1
    if jogador == n:
        acertou = True
    else:
        if jogador < n:
            print('Mais...Tente novamente.')
        elif jogador > n:
            print('Menos...Tente novamente.')
print('Acertou com {} tentativas!'.format(palpites))