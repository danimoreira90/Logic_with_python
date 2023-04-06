import datetime
a=int(input('Insira seu ano de nascimento: '))

a1= datetime.date.today().year
i = a1 - a
if i < 9:
    print('Categoria \033[0;32mMIRIM\033[m')
elif 9 <= i < 14:
    print('Categoria \033[0;35mINFANTIL\033[m')
elif 14 <= i < 19:
    print('Categoria \033[0;33mJUNIOR\033[m')
elif 19 <= i <= 20:
    print('Categoria \033[0;34mSÊNIOR\033[m')
else:
    print('Categoria \033[0;31mMASTER\033[m')