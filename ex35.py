#desenvolva um programa que leia a distancia de 3 reta  e diga ao usuario se elas podem ou nao forma um triangulo !
print('-='*20)
print('Analisador de triangulos !')
r1=int(input('digite o tamanho da primeira reta !').title())
r2=int(input('digite o tamanho da segunda reta  !').title())
r3=int(input('dgite o tamanho da terceira reta !').title())
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
     print(f'os seguimentos acima podem forma triangulo !')
else:
    print(f'Os seguimentos acima não podem formar triangulo !')