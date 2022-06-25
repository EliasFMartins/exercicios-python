#faca um programa qualquer  que pessa um numero e mostre o seu fatorial !
'''from math import factorial
n=int(input('digite um numero inteiro parar receber o fatorial'))
f=factorial(n)
print(f'o fatorial de {n} e {f} !')'''
n=int(input('digite um numero para caucular o seu fatorial !'))
print(f'cauculando fatorial de {n}....!',end='')
c=n
f=1#pra ser nulo multiplicação  tem q ser o numero 1 pois nx1 e igual a o numero
while c>0:
    print(f'{c}',end='')# o {c} mostra do numero ate 0 , o end pra colocar na mesma linha
    print(' x 'if c> 1 else '=',end='')#e respolsavel pelo testo do x e do = o end no final e pra junta as parada na mesma linha
    f*=c
    c-=1
print(f'{f}')
