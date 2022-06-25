#crie um programa que leia um numero inteiro e mostra na tela se ele e par ou inpar !
n=int(input('digite um numero inteiro e descubra se ele e impar ou par  !'.title()))
r= n % 2# toda a divisão de um numero par e 0 e toda a divisão de um numero impar e 1

if r == 0:
    print(f'o numero {n} e PAR !')
else:
    print(f'o numero {n} e IMPAR !')

ni=int(input('digite um numero inteiro e descubra se ele e impar ou par !').title())
ri=n %2
if ri==