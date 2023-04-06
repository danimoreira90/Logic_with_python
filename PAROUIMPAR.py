import random
v = 0
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('=-' * 20)
while True:
    computador = random.randint(0, 10)
    jogador = int(input('Diga um valor: '))
    resultado = jogador + computador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Faça sua escolha: Par ou ímpar [P/I]:')).strip().upper()[0]
    print(f"Você jogou {jogador} e o computador {computador}. O resultado foi {resultado}")
    if resultado % 2 == 0:
        print('O resultado foi PAR!')
    else:
        print('O resultado foi ÍMPAR!')
    if escolha == 'P':
        if resultado % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif escolha == 'I':
        if resultado % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print('Jogo finalizado. Você teve {} vitórias'.format(v))