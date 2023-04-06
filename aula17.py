num = [5, 6, 9, 0, 4, 7]
num[4] = 3
num.append(12)
num.insert(3, 44)
if 76 in num:
    num.remove(76)
else:
    print('Não existe o valor 76.')
num.sort()
num.pop()
print(num)
print(f'Essa lista tem {len(num)} números.')