print('=-'*20)
print('GERADOR DE P.A.')
print('=-'*20)
primeiro = int(input('Insira o primeiro termo para calcularmos sua P.A.: '))
razão = int(input('Insira a razão da P.A.: '))
cont = 1
total = 0
mais = 10
termo = primeiro
while mais != 0:
    total = total + mais
    while cont  <= total:
        print('{} →'.format(termo), end = ' ')
        termo = termo + razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais: '))
print('FIM. Progressão finalizada com {} termos mostrados.'.format(total))







