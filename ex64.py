#crie um programa que  receba varios numeros  e que so pare quando receber 999, mostrando quantos numeros foram digitados ao final
# e a soma total entre eles !
num=cont=soma=0# quando e o mesmo valor pra todos pode se colocalos na mesma linha
num=int(input('dgite  um numero inteiro'))#foi colocado o comando dentro e fora do while pois e ignorado o flag
while num!=999:#enquanto num for diferente de 999 vai continuar contando
    soma+=num#soma =soma+numero essa e a forma simplificada !
    cont+=1#cont=cont+1 tbm e a forma simplificada !
    num = int(input('dgite  um numero inteiro'))#para desconsiderar o flag
print(f'a  quantidade de numeros digitados foi {cont} e a soma deles e {soma} !')