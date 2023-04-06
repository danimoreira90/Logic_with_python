def gols_time(tabela, time):
  gols = []
  for linha in tabela:
    if linha[1] == time:
      gols.append(linha[2])
  return sum(gols)

def gols_time_lc(tabela, time):
  gols = [linha[2] for linha in tabela if linha[1] == time]
  return sum(gols)


tabela = [['Pedro', 'Flamengo', 12],
         ['Lucas', 'Vélez', 7],
         ['Rafel', 'Palmeiras', 7],
         ['Rony', 'Palmeiras', 7],
         ['Gabigol', 'Flamengo', 6]]

print('Flamengo:', gols_time_lc(tabela, 'Flamengo'))
print('Palmeiras:', gols_time_lc(tabela, 'Palmeiras'))