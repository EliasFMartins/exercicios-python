#crie um programa q  mostre de 1 a 50 todos os numeros pares entre eles !
from time import sleep
x=str(input('digite ok para receber a sequencia de numeros pares !').upper())
if x=='OK':
    print('Startando !!!'.upper())
    sleep(1)
    print('processando requisição ...')
    sleep(2)
    for c in range(0,50,2):
        print(c)
print('sequencia finalizada !!!!')