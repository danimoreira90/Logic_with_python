p=float(input('Insira o Valor do produto em R$: '))
cp=str(input('Insira a condição de pagamento: ')).strip()
if cp.find('dinheiro/cheque'):
    print('Você pagará R${}'.format(p-(p*10)/100))
if cp.find('cartão'):
    print('Você pagará R${}'.format(p-(p*5)/100))