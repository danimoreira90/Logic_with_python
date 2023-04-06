print('__'*20)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('__'*20)
listagem = ('Espada', 27.55, 'Escudo', 30.40, 'Arco', 40.75, 'Armadura', 120.75,
            'Talismã', 70.90, 'Botas', 20.60, 'Luvas', 15.45, 'Elmo', 35.60)
print(f'''{listagem[0]}...................$  {listagem[1]:.2f}
{listagem[2]}...................$  {listagem[3]:.2f}
{listagem[4]}.....................$  {listagem[5]:.2f}
{listagem[6]}.................$  {listagem[7]:.2f}
{listagem[8]}..................$  {listagem[9]:.2f}
{listagem[10]}....................$  {listagem[11]:.2f}
{listagem[12]}....................$  {listagem[13]:.2f}
{listagem[14]}.....................$  {listagem[15]:.2f}''')