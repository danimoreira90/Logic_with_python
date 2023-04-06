def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido\033[m.')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31mO usuário preferiu não digitar o valor.\033[m')
            return 0
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mO usuário preferiu não digitar esse valor.\033[m')
            return 0
        else:
            return n


n1 = leiaint('Digite um valor inteiro: ')
n2 = leiafloat('Digite um valor real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}.')