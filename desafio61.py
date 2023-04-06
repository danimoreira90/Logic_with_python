
sexo = str(input('Digite seu sexo: ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Digite seu sexo: ')).upper().strip()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))



