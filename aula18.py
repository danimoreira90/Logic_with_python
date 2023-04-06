teste = []
teste.append('Daniel')
teste.append(32)
galera = []
galera.append(teste[:])
teste[0] = 'Bauer'
teste[1] = 33
galera.append(teste[:])
print(galera)
