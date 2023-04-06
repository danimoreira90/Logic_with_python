import time
l = [i for i in range(8000000)]
inicio = time.time()
print(99999999999 in l)
fim = time.time()
print(f'{(fim - inicio):.7f}')


c = {i for i in range(8000000)}
inicio = time.time()
print(99999999999 in c)
fim = time.time()
print(f'{(fim - inicio):.7f}')