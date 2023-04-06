# abre o arquivo para leitura
dados = open('ex-leitura.txt', 'r')

# lê primeira linha
linha = dados.readline()

while linha != '':              # enquanto não é o fim...
    print(linha, end='')        # mostra na tela
    linha = dados.readline()    # lê próxima linha

dados.close()                   # fecha o arquivo