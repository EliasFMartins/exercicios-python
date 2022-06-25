#melhore o jogo  do desafio 28  faça o computador escolher um numero de 1 ate 10 e caso erre vc terar q digitar ate acertar
# e no final mostre quantas tentativas vc precisou pra acertar !
from random import randint
pc=randint(1,10)#randonisou um numero entre 1 e 10
print('sou o seu pc, acabei de pensar em um numero de 1 a 10 !')
print('sera que vc consegue adivinhar qual foi ?')
acertou=False
palpits=0
while not acertou :#enquanto acertou n se torna verdadeiro vai se repetir o input!
    jogador=int(input('qual e o seu palpite ? '))
    palpits+=1
    if jogador==pc:
        acertou = True# a condição de se ele acertar se tornar verdadeiro assim parando o while ! com so 1 = recebe  com 2 e igual !
    else:
        if pc>jogador:
            print('tente um numero maior meu nobre !')
        elif pc<jogador:
            print('tente um numero menor grande homem !')
print(f'parabens vc consegui !!!!'.upper())
print(f'vc precisou de {palpits} papits pra acertar fera !!!')