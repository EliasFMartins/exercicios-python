#desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles q forem pares
#se o valor digitado for impar desconsidere-o

soma=0
cont=0

for c in range(1,7):
    n=int(input('digite  um numero inteiro !'))
    if n%2==0:#a condição do if serviu pra filtar  numeros  divididos por 2 com resto igual a 0 com o % tudo q esta
        #dentro pro causa do endentamento aplica a função do if rever essa merda e mt importante !!!
        soma+=n# esta da forma simplifacada seria soma +soma= n
        cont+=1# esta simplificado seria cont=cont+1
print(f' a quantidade de numeros  Pares e a soma foi {cont} a soma dos numeros foi {soma} !')