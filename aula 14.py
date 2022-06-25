'''for c in range(1,10):
print('c)
print:fim'''
par=impar=0
c=1
while c !=0:
    c=int(input('digite um numero !'))
    if par % 2==0:
        par=par+1
    else:
        impar=impar+1
print(f'vc digitou {par} numeros pares e {impar} numeros impares !')