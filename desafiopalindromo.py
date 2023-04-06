import random
import time
lista = ('PEDRA', 'PAPEL', 'TESOURA')

print('{:=^40}'.format('JOKEMPO!'))
print('''Insira a opção da sua jogada
[0]PEDRA
[1]PAPEL
[2]TESOURA''')
jogada=int(input('Opção a jogar: '))

computador=random.randint(0,2)
time.sleep(1)
print('JO...')
time.sleep(1)
print('KEN...')
time.sleep(1)
print('PO!!!')
print('O computador escolheu {}'.format(lista[computador]))
print('O jogador jogou {}'.format(lista[jogada]))
if computador == 0:
    if jogada == 0:
        print('EMPATE!')
    elif jogada == 1:
        print('VOCÊ VENCEU!')
    elif jogada == 2:
        print('O COMPUTADOR VENCEU. Tente novamente.')
    else:
        print('JOGADA INVÁLIDA')


if computador == 1:
    if jogada == 0:
        print('O COMPUTADOR VENCEU. Tente novamente.')
    elif jogada == 1:
        print('EMPATE!')
    elif jogada == 2:
        print('VOCÊ VENCEU!')
    else:
        print('JOGADA INVÁLIDA')


if computador == 2:
    if jogada == 0:
        print('VOCÊ VENCEU!')
    elif jogada == 1:
        print('O COMPUTADOR VENCEU. Tente novamente.')
    elif jogada == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA')

