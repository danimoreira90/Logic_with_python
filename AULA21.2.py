#PARÂMETROS OPCIONAIS
def somar(a=0, b=0, c=0): #<----- PARÂMETRO OPCIONAL
    s = a + b + c
    print(f'A soma vale {s}.')

somar(2, 4, 8)
somar()
somar(c=3, a=654)
somar(b=56)