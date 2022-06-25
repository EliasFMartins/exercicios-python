#faça um programa que leia o ano de nsacimento de um jovem e informe  de acordo com a sua idade
#se ele ainda vai se alistar  ao serviço militar,se e a hora de se alistar, se ja passou do tempo de alistamento
# o programa tbm devera mostar o tempo q falta ou que passou do prazo de alistamento !
from datetime import date
an=int(input('digite o ano em que vc nasceu !!!'))
a=date.today().year
idade= a-an
saldo=idade-18
tp=a-saldo
if idade<18:
    print(f'vc tem {idade} anos faltam {saldo} para vc se alistar !')
    print(f'vc deveria se alistar em {tp} !')
elif idade>18:
    print(f'vc tem {idade} ja passou {saldo} anos do tempo correto q vc deveria se aprensetar !!')
    print('se aprensete a  om mas proxima pra fazer o alistamento !!'.upper())
    print(f'o ano em que vc deveria se alistar e {tp}')
elif idade==18:
    print(f' vc tem {idade} anos e deverar se alistar nas forças armadas esse ano !')
    print(' não deixe de comparecer !!'.upper())
#fazer as variaveis pra facilitar essa merda .... tnc viu