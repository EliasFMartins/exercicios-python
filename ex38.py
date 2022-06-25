#escreva um programa que leia dois numeros inteiros e compare-os mostrando na tela uma msg
# o primeiro valor e maior , o segundo valor e maior ,não existe valor maior , os dois sâo iguais
n1=int(input('digite  um numero inteiro !'))
n2=int(input('digite outro numero inteiro'))
if n1<n2:
    menor=n1
    print(f'os numeros digitados foram {n1, n2} o {menor} e o menor e o {n2} eo maior !')
elif n1==n2:
    print(f' ambos os numeros {n1, n2} são iguais !!')
else:
    print(f'os numeros digitados foram {n1, n2} o {n2} e menor  que {n1} !')