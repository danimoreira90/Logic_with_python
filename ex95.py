from time import sleep
def maior(* valores):
    mai = men = 0
    cont = 0
    print('-='*25)
    print('Analisando os valores informados...')
    sleep(2.0)
    print(valores, end='', flush=True)
    sleep(0.5)
    print(f' Foram informados {len(valores)} no total ')
    print(f'O maior valor informado foi {max(valores)}')



maior(1,8,7,6,5,4,3)
maior(5,67,4,3,8)
maior(0)
maior(-4, 3, 7, 567)

