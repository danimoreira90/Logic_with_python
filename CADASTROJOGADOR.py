
player = {}
totgols = []
pont = 0
gols = []
player['Nome'] = str(input('Nome do Jogador: '))
player['Partidas'] = int(input(f'Quantas partidas {player["Nome"]} jogou? '))
player['Gols'] = totgols
player['Total de Gols'] = pont
for c in range(0, player["Partidas"]):
    gols = int(input(f'Quantos gols {player["Nome"]} marcou na {c+1}ª partida?  '))
    totgols.append(gols)
    pont += gols
player['Total de Gols'] = pont
print('=-'*40)
print(player)
print('=-'*40)
for keys, values in player.items():
    print(f'O Registro {keys} tem informativo {values}.')
print('=-'*40)
print(f'O jogador {player["Nome"]} jogou {player["Partidas"]} partidas.')
for i, v in enumerate(totgols):
    print(f'   => Na {i+1}ª partida {player["Nome"]} fez {v} gols. ')
print(f'{player["Nome"]} fez um total de {pont} gols.')




