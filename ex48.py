#faça um programa que calcule a soma entre todos os numeros impares que são multiplos de tres e que se
#emcpmtra, mo intervalo de 1 a 500
soma=0
cont=0
for c in range(1,501 ,2):#COMECOU  com no 1 ate 501  contando de 2 em dois como comecou com impar terminou com impar
    if c % 3==0:# somente os divisiveis por 3  , serviu pra filtar  !!
        cont=cont+1#contou todos os numeros subistituindo o valor anterior e adicionado mas 1
        soma=soma+c #somou o valor do anterior com o proximo
print(f'a soma dos {cont} valores solicitados e {soma}')
