#elabore um programa que caucule o valor a ser pago por um produto,considerando seu preco normal e condição de pagamento
#a vista dinheiro /cheque:10% de desconto,a vista no cartao :5% de desconto -em  ate 2x no cartao presco normal
#3x ou mais  no cartão  20% de juros ...
print('{:=^40}'.format('loja green ').upper())
preço=float(input('digite o valor a ser pago !'))
forma=int(input('''Escolha a forma de pagamento a baixo !
[ 1 ] Dinheiro ou Cheque !
[ 2 ] A vista no Cartão !
[ 3 ] Ate 2x no cartão !
[ 4 ] 3x ou mais no cartão !'''))
if forma== 1:
    total=preço-(preço*10/100)
    desconto=f'vc recebeu um desconto de {preço-total} nessa modalidade !'
elif forma ==2:
    total=preço-(preço*10/100)
    desconto=f'vc recebeu um desconto de {preço-total:.2f} nessa modalidade !'
elif forma==3:
    total=preço
    desconto='não a  desconto nessa modalidade !'
elif forma==4:
    total=preço+(preço*20/100)
    parcelas=int(input('digite a quantidade de parcelas que deseja dividir !'))
    print(f' a sua compra foi dividida em  {parcelas} parcelas de R${total/parcelas} !')
    desconto=f' vc teve um acrecimo de R$ {total-preço} nessa forma de pagamento !'
else:
    print(f'opção invalida , tente novamente !!!'.upper())
print(f'o valor a sua compra e de R$ {preço} e vai sair pór R${total} ')
print(f'{desconto}')


