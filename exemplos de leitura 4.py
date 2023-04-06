# abre o arquivo para leitura
dados = open('ex-leitura.txt', 'r')

# lê todas as linhas para uma lista
linhas = dados.readlines()

# iterando sobre a lista...
for linha in linhas:
    print(linha, end='')    # mostra na tela

dados.close()               # fecha o arquivo