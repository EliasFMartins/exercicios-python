#faca um programa que leia um numero inteiro e diga se ele e ou não um numero primo !
n=int(input('digite um numero inteiro'))
tot=0
for c in range(1,n+1):  # fico esse n+1 pq o ultimo numero não aparece !!!
    if  n % c == 0 :
        print(f'\033[34m', end= ' ')
        tot += 1
    else:
        print(f'\033[33m', end= ' ')
        print(f'{c}',end=' ')
print(f'\33[0m numero {n} divisivel por {tot} vezes !')
if tot==2:
         print(f'por isso e PRIMO') # e considerado primo se for dividido por 1 e por ele mesmo ou seja por 2
else:
        print(f'por isso nao e PRIMO')# caso seja considerado divisivel por mais de 2 ja não e considerado primo !