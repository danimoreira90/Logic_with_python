n1 = int(input('Insira o primeiro valor: '))
n2 = int(input('Insira o segundo valor: '))
menu = int(input('''Escolha a opção desejada:
[1]Soma
[2]Multiplicação
[3]Maior valor
[4]Novos números
[5]Finalizar programa'''))
while menu != 5:
    if menu == 1:
        soma = n1 + n2
        print('A soma do primeiro e do segundo valor é {}'.format(soma))
    if menu == 2:
        mult = n1*n2
        print('O produto entre o primeiro e o segundo valor é {}'.format(mult))
    if menu == 3:
        if n1 > n2:
            print('O primeiro valor é maior que o segundo')
        else:
            print('O segundo valor é maior que o primeiro')
    if menu == 4:
        print('Insira novos valores: ')
        n1 = int(input('Insira o primeiro valor: '))
        n2 = int(input('Insira o segundo valor: '))

        print('Programa finalizado.')

    menu = int(input('''Escolha a opção desejada:
    [1]Soma
    [2]Multiplicação
    [3]Maior valor
    [4]Novos números
    [5]Finalizar programa'''))

print('Programa finalizado.')
