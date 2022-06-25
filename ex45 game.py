#crie um programa que faça o computador jogar jokenpo com vc ....
from random import randint
import time
print('jo ken pow !'.upper())
print('''suas opções !
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
lista=('PEDRA','PAPEL','TESOURA')
pc=randint(0,2)
e=int(input('escolha a  entre os itens acima !'))
print('JO')
time.sleep(1)
print('ken')
time.sleep(1)
print('po')
time.sleep(2)
print('=-'*10)
print(f'o escolhido foi  computador foi {lista[pc]} !')
print(f" a sua escolha foi {lista[e]}")
print('=-='*10)
if pc==0:# pc escolheu pedra !!
    if e==0:
        print('empate !')
    elif e==1:
        print('você ganhou !')
    elif e==2:
        print('vc perdeu !')
    else:
        print('opção invalida !!')
elif pc==1:#pc escolheu  papel !!
    if e==0:
        print('vc perdeu !')
    elif e==1:
        print(('empate !'))
    elif e==2:
        print('vc ganhou !!')
    else:
        print('opção invalida !!')
elif pc==2:#pc escolheu tesoura
    if e==0:
        print('vc ganhou !')
    elif e==1:
        print('vc perdeu !!')
    elif e==2:
        print('empate !!')
    else:
        print('opção invalida !!')
