#ESCOPO DE VARIÁVEIS.2
def teste(b):
    global a # DEI A ORDEM PARA USAR A VARIÁVEL GLOBAL "a", AGORA A VARIÁVEL DENTRO DA FUNÇÃO SE TORNARÁ GLOBAL.
    a = 8 #<-------- "a" LOCAL
    b +=4 #<-------- ESCOPO LOCAL
    c = 2 #<-------- ESCOPO LOCAL
    print(f' "a" dentro vale {a}.') # VALERÁ 8, POIS É 'LOCAL'.
    print(f' "b" dentro vale {b}.') # CONTINUARÁ VALENDO 9, POIS SOMARÁ COM O "a" GLOBAL.
    print(f' "c" dentro vale {c}.')


a = 5   # <-------- ESCOPO GLOBAL
teste(a)
print(f' "a" fora vale {a}.')
