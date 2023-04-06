def processa_resultado(num_1, num_2):
  result = (num_1 + num_2) % 2
  return result


def imprime_resultado(resp, jog_par, jog_impar):
  print(f'\n Resultado Par, venceu o jogador(a) {jog_par} ') if resp == 0 else print(f'\n Resultado Ímpar, venceu o jogador(a) {jog_impar} ')


def inicio():
  jogador_Par, jogador_Impar = input('Informe o nome do jogador(a), opçãoo PAR: '), input('Informe o nome do jogador(a), opçãoo ÍMPAR: ')

  try:
    num_jogador_Par, num_jogador_Impar = int(input(f'Jogador(a) {jogador_Par}, informe seu número: ')), int(input(f'Jogador(a) {jogador_Impar}, informe seu número: '))
  except:
    print('\nOps... você errou!\nDa próxima vez digite um número inteiro. Comece novamente...\n')
    inicio()
  else:
    resp = processa_resultado(num_jogador_Par, num_jogador_Impar)
    imprime_resultado(resp, jogador_Par, jogador_Impar)




inicio()