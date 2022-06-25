#faça um programa que joguei par ou impar com o computador e mostre o total de vitorias consecutivas  !
from random import randint#importa a bibliotaeca  radom
v=0
while True:#condição de repetição infinita
    jogador=int(input('digite um numero !'))
    computador=randint(0,10)#sortear um numero aleatorio entre 0e9
    total=jogador+computador#somar os valores
    tipo=' '#o tipo fica vazio ate receber o valor do input la enbaixo
    while tipo not in'PI':
        tipo=str(input('par ou impar [ P ]/[ I] !')).upper().strip()[0]#vai passar pra letra maiuscula vai tirar os espaços e pegar a primeira letra
    print(f'voçê jogou {jogador} e o computador jogou {computador} , total de {total} ',end='')
    print(f' DEU PAR 'if total % 2==0 else 'DEU IMPAR !')#forma simplificada  de if e else , deu par se , o o oposto
    if tipo=='P':#tipo e igual a par digitado anteriormente !
        if total % 2 == 0:#total  dividido por 2 se o resto for zero e par
           print('vc ganhou !!'.upper())
           v+=1
        else:
            print('você perdeu!!'.upper())
            break
    elif tipo=='I':
        if total % 2 == 1:#numeros impares divididos por 2 dao resto 1
            print('vc ganhou !!')
            v+=1
        else:
            print('vc perdeu !!!'.upper())
            break
    print('vamos jogar novamente'.capitalize())
print(f' gamer ouver  vc ganhou {v} partida ')