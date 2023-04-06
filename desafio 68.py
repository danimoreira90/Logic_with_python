print('-' * 40)
print('{:^40}'.format('PROGRAMA TABUADA'))
print('-' * 40)
while True:
   n = int(input('Insira um número para calcular sua tabuada:'))
   if n < 0:
      break
   for c in range (1, 11):
      print(f'{n} x {c} = {n*c}')

print('PROGRAMA FINALIZADO.')
