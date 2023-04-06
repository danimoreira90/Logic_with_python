frase = str(input('Insira sua frase: ')).strip().upper()
palavras = frase.split()
junto =''.join(palavras)
inverso =''
for letra in range (len(junto)-1, -1, -1):
    inverso = inverso + junto[letra]
print(junto, inverso)
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo!')