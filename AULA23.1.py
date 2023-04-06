try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou'
          '.')
else:
    print(f'O resultado é {r}.')
finally:
    print('Volte sempre! Muito obrigado!')