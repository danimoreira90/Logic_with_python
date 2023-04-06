clubes = ('América-MG', 'Athletico-PR', 'Atlético-GO', 'Atlético-MG',
          'Avaí', 'Botafogo', 'Ceará', 'Corinthians', 'Coritiba', 'Cuiabá',
          'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Internacional',
          'Juventude', 'Palmeiras', 'Bragantino', 'Santos', 'São Paulo')
print('=-='*20)
print(f'Lista de times do Brasileirão: {clubes}')
print('=-='*20)
print(f'Os 5 primeiros da lista são {clubes[0:5]}')
print('=-='*20)
print(f'Os quatro últimos da lista são {clubes[16:20]}')
print('=-='*20)
print(f'Os times em ordem alfabética são: {sorted(clubes)}')
print('=-='*20)
print(f'O Bragantino está na {clubes.index("Bragantino")+1}ª posição  ')