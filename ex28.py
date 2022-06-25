#escreva um programa q faça o computador pensar em um numero inteiro de 0 a 5 e fazer o usuario tentar advinhar
#escolher randonicamente , e mostrar se vc acertou ou nao o numero e mostre na tela!in
from random import choice#a pela função randint eu poderia ter colocado so (1,5) e ele ia randonizar um numero entre esses
from time import sleep # a biblioteca  faz uma pequena pausa com sleep e vc coloca os segundos ().
n=int(input('O computador vai escolher um numero aleatorio de 0 a 5, tente advinhar !'))
lista=[0,1,2,3,4,5]
escolha=choice(lista)
print('=-=-=-=-='*20 )
print('processando ...')
sleep(2)
if n==escolha:
    print(f'o numero que vc escolheu foi {n} o numero escolhido pelo pc e{escolha} ')
    print('Parabens vc e Incrivel !')
else:
    print(f'infeliz vc errou, o numero escolhido foi pelo PC foi {escolha}  mais sorte na proxima')

    '''exemplo 2 !!'''

'''from random import randint#a pela função randint eu poderia ter colocado so (1,5) e ele ia randonizar um numero entre esses
from time import sleep
from time import sleep # a biblioteca  faz uma pequena pausa com sleep e vc coloca os segundos ().
n=int(input('tente adivinhar o numero aleatorio  q eu  vou escolher  de 1 a 9'.title()))
l=randint(1,2)
print('processando...'.upper())
sleep(1)
if n==l:
    print(f'o numero sorteado foi {l} e vc escolheu o numero  {n} !'.capitalize())
    print(('parabens vc ganhou !'.upper()))
else:
    print(f'o numero sorteado foi {l} e vc escolheu o numero {n} !'.capitalize())
    print('infelizmente vc não ganhou , mais sorte na proxima !'.upper())'''