from datetime import date
def voto(an=0):
    if 65 > date.today().year - an > 18:
        return print(f'Com {date.today().year - an} anos, VOTO OBRIGATÓRIO.')
    if date.today().year - an < 18:
        return print(f'Com {date.today().year - an} anos, VOTO NEGADO.')
    if date.today().year - an > 65:
        return print(f'Com {date.today().year - an} anos, VOTO OPCIONAL')

an = int(input((f'Em que ano você nasceu? ')))
voto(an)

