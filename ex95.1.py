from time import sleep


def maior(* num):
    mai = 0
    cont = 0
    print('-='*25)
    print('Analisando os valores informados...')
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.3)
        if cont == 0:
            mai = valor
        else:
            if valor > mai:
                mai = valor
        cont += 1
    print(f'Foram informados {cont} valores.')
    print(f'O maior valor informado foi {mai}.')






maior(1,8,7,6,5,4,3)
maior(5,67,4,3,8)
maior(0)
maior(-4, 3, 7, 567)