def area(larg, comp):
    area = (larg * comp)
    print(f'A área de um terreno de {larg}m x {comp}m é de {area}m².')


print('CONTROLE DE TERRENOS')
print('_'*20)
l = float(input('LARGURA em (m): '))
h = float(input('COMPRIMENTO em (m): '))
area(l, h)




