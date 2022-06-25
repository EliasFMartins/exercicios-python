saque=int(input('digite o valor do saque R$:'))
print('*^'*20)
for notas in [50,20,10,5,1]:
    quant = saque // notas
    valor = saque % notas
    if quant > 0:
        print(f'o total de {quant}  notas e {notas}')

'''valorSaque = int(input('Valor do saque: R$ '))
print('-' * 40)
for nota in [50, 20, 10, 5, 2, 1]:
    quantidade = valorSaque // nota
    valorSaque = valorSaque % nota
    if quantidade > 0:
        print(f'{quantidade} notas de R$ {nota}')'''