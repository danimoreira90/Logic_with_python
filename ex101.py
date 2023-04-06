def fatorial(num=1, show=False):
    """
fatorial(n, show=False)
    -->Calcula o fatorial de um número.
    :param num:O número a ser calculado.
    :param show:(Opcional) Mostrar ou não o processo de conta.
    :return:O valor do Fatorial de um número "n".
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c

    if show == True:
        c = num
        while c > 0:
            print(f'{c}', end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(f' = ', end='')
            c -= 1

    return f
print('=-'*25)
print(fatorial(9, show=True))
help(fatorial)