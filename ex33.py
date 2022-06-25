#faca um programa que leia 3 numeros e mostre qual e o maior e qual e o menor deles !
n=int(input('digite um numero inteiro !'))
n2=int(input('digite um outro numero inteiro !'))
n3=int(input('digite mais um numero inteiro !'))
menor=n

if n2<n and n2<n3: #ordem  se , e  achei mt foda
    menor=n2
if n3<n2 and n3<n:
    menor=n3
maior=n

if n2>n and n2>n3:
    maior=n2
if n3>n and n3>n2:
    maior=n3
print(f'o maior numero e {maior} e o menor numero e {menor} !')


'''versão maior
n1=float(input('digite um numero !.'.capitalize()))
n2=float(input('digite outro numero !'.capitalize()))
n3=float(input('digite outro numero !'.capitalize()))
n4=float(input('digite mas um numero !'.capitalize()))
m=n1
if n2<n1 and n2<n3 and n3<n4:
    m=n2
if n3<n2 and n3<n4 and n3<n1:
    m=n3
if n4<n1 and n4<n2 and n4<n3:
    m+n4
ma=n1
if n2>n1 and n2>n3 and n2>n4:
    ma=n2
if n3>n1 and n3>n2 and n3>n4:
    ma=n3
if n4>n1 and n4>n2 and n4>n3:
    ma=n4
print(f'o maior valor e  {ma}  !\n'
      f'o menor valor e {m} ! '.upper())
'''