def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}.')


soma(4, 9)
soma(5, 8, 5, 7, 9)
soma(9, 1, 4)
