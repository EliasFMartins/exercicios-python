from time import sleep
from random import randint
print(f'vamos jogar um game ....')
sleep(3)
print(f'''digite  um numero pra escolher a opção desejada !!
[ 1 ] pedra !
[ 2 ] papel !
[ 3 ] tesoura !''')
e=int(input('digite a opção escolhida !!!'))
pc=randint(1,2,3)
if e==pc:
    print(f'a sua escolha foi')