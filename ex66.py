#crie  um programa que leia numeros infinitos ate receber 999 e mostre a soma entre eles e quantos foram digitados
soma,cont=0,0
while True:
        numero = int(input('insira um valor !'))
        if numero==999:
            break
        cont+=1#tbm tem q ficar enbaixo do break se n e contabilizado '-'
        soma += numero#sapoha tem q ficar enbaixo do  break para n contabilizar o flag...
print(f'fim')
print(f'a quantidade de numeros digitados foi de {cont} e soma entre os numeros digitados e {soma}')