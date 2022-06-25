# crie um programa que pessa ao usuario 2 numeros  e  em seguida mostre um menu  perguntando oque o usuario quer fazer a seguir
#multiplicar , somar  qual e o maior , novos numeros  e sair do programa , tem quue ser funcional essapoha heim
from time import sleep
n1=int(input('digite um numero inteiro '))
n2=int(input('digite outro numero inteiro '))
op=0
while op != 5:
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] qual e o maior
    [ 4 ] inserir novos numeros
    [ 5 ] sair do programa ''')
    op=int(input('>>> Qual e a sua opção ?'))

    if op==1:
        resultado = n1+n2
        print(f'a soma de {n1} + {n2}  e igual a {resultado} !')
    elif op==2:
        produto = n1* n2
        print(f'a multiplicação de {n1} e {n2}  e igual a {produto} !')
    elif op==3:
        if n1<n2:
         menor=n1
        else:
            menor=n2
        print(f'dos numeros {n1} e {n2} o menor e {menor} !')
    elif op==4:
        print('insira os novos valores ')
        n1=int(input('digite o primeiro valor'))
        n2=int(input('digite o segundo valor '))

    elif op==5:
        print('aguarde enquanto o programa e finalizado ...')
        sleep(2)
        print('o programa esta sendo finalizado ...')
        sleep(3)

    else:
        print('opção invalida aguarde e tente novamente  ...')
        sleep(3)
print('=-=-='*20)
print('fim do programa volte sempre !!!'.upper())
