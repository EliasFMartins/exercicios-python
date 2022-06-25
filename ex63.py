#escreva um programa que leia  um numero inteiro e mostre na tela os primeiros  numeros da sequencia de fibonnati
print('-='*20)
print('sequiencia de fiboncacci')
print('-=-'*10)
n=int(input('digite quantos termos vc quer mostar '))
t1=0
t2=1
print('~'*20)
print(f'{t1} ,{t2}',end='')
cont=3
while cont <= n:
        t3 = t1 + t2
        print(f'-> {t3}',end='')
        t1 = t2
        t2 = t3
        cont += 1
print(' fim')
