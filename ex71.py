#crie um programa que simule o funcionamento de um caixa eletronico , no inicio pergunto ao usuario o valor a ser sacado
# e o programa vai lhe informar quantas sedulas serão sacadas  considere cedulas de 50, 20 10 e 1
print('='*40)
print('{:^30}'.format('banco bb').upper())
print('='*40)
valor=int(input('qual valor vc deseja sacar ?'.upper()))
total=valor
ced=50
totalcd=0
while True:
    if total>=ced:
        total-=ced
        totalcd+=1
    else:
        if totalcd>0:
            print(f'total de {totalcd}  cedulas de {ced}')
        if ced==50:
            ced=20
        elif ced==20:
            ced=10
        elif ced==10:
            ced=1
        totalcd=0
        if total ==0:
            break

print('='*40)
print('volte sempre ao banco '.upper())
