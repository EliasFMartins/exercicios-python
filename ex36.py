#faça um programa  para aprovar o emprestimo bancario para a compra de uma casa . o programa vai perguntar o valor da casa , o salario do comprador
#e  em quantos anos ele vai pagar  caucule o valor da prestação mensal sabendo que ela nao pode exceder 30% do salario ou então o emprestimo sera negado !
vc=float(input('digite o valor da casa a ser finaciada pelo banco: R$!!'))
s=float(input('digite o valor da renda  do comprador  !!: R$'))
t=int(input('digite em quantos anos  sera feito o finaciamento do imovel !!: '))
p=vc/(t*12)
m=s*30/100
print(f'para pagar um finaciamento de {vc} em {t} anos',end=' >>')
print((f'a prestação ficara em {p:.2f} reais !'))
if p<=m:
    print(f'emprestimo PODE SER CONCEDIDO !!!')
else:
    print('imprestimo NÂO CONCEDIDO!!!')

'''BASTANTE ATENÇAO TENTEI FAZER ESSE EXERCICIO DE UMA VEZ E N CONSEGUI !!!
SEMPRE QUE ISSO OCORRER FAZER POR PARTES E DECLARAR VARIAVEIS PRA FACILITAR 
TANTO O ENTENDIMENTO E PRA SIMPLIFICAR AS COISAS !!!!'''