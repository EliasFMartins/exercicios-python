#crie um programa  que ao final da execução mostre a media entre eles , alem de qual e o maior e o menor valor
# o programa tbm deve perguntar ao usuario se ele quer  continuar ou n !
n=c=maior=menor=0
p='s'
soma=0
while p in'sS':# a condição enquanto p for s ou S  ele vai continuar
    n=int(input('digite um numero'))
    soma+=n
    c+=1
    if c==1:
        maior=menor=n
    else:
        if n>maior:
            maior=n
        if n<menor:
            menor=n
    p = str(input('deseja continuar [ S / N ]')).upper().strip()[0]  # pra pegar somente a primeira letra  , caso a pessoa venha a digitar sim neh
media=soma/c
print(f'vc digitou {c} numeros a media entre eles e {media:.2f} ')
print(f'o maior valor foi {maior} e o menor valor foi {menor} !')