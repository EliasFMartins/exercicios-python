#faça um programa que mostre na tela uma contagem regressiva para o estourop de fogos de artificio
#que va de 10 a 0, com uma pausa de 1 segundo entre eles
from time import sleep

x=input('digite ok pra continuar').upper()
if x=='OK':
    for c in range(10,0,-1):
     print(c)
     sleep(1)
else:
    print('error tente novamente !'.upper())
print('end!')
print('I Happy new world'.upper())
