preço = float(input('Insira o valor do produto em R$: '))
print('[0]à vista dinheiro/cheque: 10% de desconto'
'\n[1]à vista no cartão: 5% de desconto \n[2]Em até 2x no cartão: preço formal\n[3]3x ou mais no cartão: 20% de juros')
pagamento = int(input('Insira a opção de pagamento: '))

if pagamento == 0:
    print('Você recebeu 10% de desconto e pagará R${}'.format(preço-(preço*10)/100))
if pagamento == 1:
        print('Você recebeu 5% de desconto e pagará R${}'.format(preço-(preço*5)/100))
if pagamento == 2:
    print('Você pagará o preço formal de R${}, sendo sua parcela R${}'.format(preço, (preço)/2))
elif pagamento == 3:
    print("Você terá 20% de juros, sendo o valor total R${} e sua parcela R${}".format(((preço + (preço * 20) / 100))),
          (((preço+(preço*20)/100))) / 3)
