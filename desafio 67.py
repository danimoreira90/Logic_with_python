n = s = cont = 0
while True:
    n = int(input('Digite um número:'))
    s += n
    cont += 1
    if n == 999:
        s -= 999
        cont -= 1
    if n == 999:
        break

print(f'A soma entre os números foi de {s} e o total de números somados foi de {cont}.')