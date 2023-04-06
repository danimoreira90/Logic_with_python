#ESCOPO DE VARIÁVEIS
def teste(b):
    b +=4 #<-------- ESCOPO LOCAL
    c = 2 #<-------- ESCOPO LOCAL
    print(f' "a" dentro vale {a}.')
    print(f' "b" dentro vale {b}.')
    print(f' "c" dentro vale {c}.')


a = 5   # <-------- ESCOPO GLOBAL
teste(a)
print(f' "a" fora vale {a}.')
print(f' "b" fora vale {b}.') #<-----ERRO POR FALTA DE ESCOPO
print(f' "c" fora vale {c}.') #<-----ERRO POR FALTA DE ESCOPO