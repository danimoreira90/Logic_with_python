#ESCOPO DE VARIÁVEIS.1
def teste(b):
    a = 8 #<-------- "a" LOCAL
    b +=4 #<-------- ESCOPO LOCAL
    c = 2 #<-------- ESCOPO LOCAL
    print(f' "a" dentro vale {a}.') # VALERÁ 8, POIS É 'LOCAL'.
    print(f' "b" dentro vale {b}.') # CONTINUARÁ VALENDO 9, POIS SOMARÁ COM O "a" GLOBAL.
    print(f' "c" dentro vale {c}.')


a = 5   # <-------- ESCOPO GLOBAL
teste(a)
print(f' "a" fora vale {a}.')
print(f' "b" fora vale {b}.') #<-----ERRO POR FALTA DE ESCOPO
print(f' "c" fora vale {c}.') #<-----ERRO POR FALTA DE ESCOPO