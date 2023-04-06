# abre o arquivo para leitura
dados = open('ex-leitura.txt', 'r')

# usando um iterador para ler linha a linha...
for linha in dados:
    print(linha, end='')    # mostra na tela

dados.close()               # fecha o arquivo