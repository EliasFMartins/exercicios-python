#crie um programa que leia a idade e o sexo de varias pessoas ao terminio do programa ele deve falar quantos h quantas mulheres abaixo de 20 anos
# e quantas pessoas tem mais de 18 anos
tot18=toth=totm20=0
while True:
    idade=int(input('qual  a sua idade  ?'))
    sexo=' '
    while sexo not in 'M,F':
        sexo=str(input('qual e o seu sexo [ M ]/[ F ] !')).upper().strip()[0]
    if idade>=18:
        tot18+=1
    if sexo=='M':
        toth+=1
    if sexo=='F' and idade<20:
        toth+=1
    resposta=' '
    while resposta not in 'SN':
        resposta=str(input('quer continuar [ S ]/[ N ]')).upper().strip()[0]
    if resposta == 'N':
        break
print(f'o total de pessoas maiores de 18 anos são {tot18}')
print(f'o total de homems cadatrados e {toth} !')
print(f'o total de mulheres cadatradas abaixo de 20 anos são {totm20}')