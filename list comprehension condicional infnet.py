linha = input()

# usando list comprehension E expressão condicional c/ if else
lista = [palavra.capitalize() if palavra.startswith('m') else palavra
         for palavra in linha.split()]

# usando estruturas de repetição e condicional convencionais
for palavra in linha.split():
  if palavra.startswith('m'):
    lista.append(palavra.capitalize())
  else:
    lista.append(palavra)