#desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. no final do programa mostre:
#a media de idade do grupo, qual o nome do homem mais velho.e quantas mulheres têm menos de 20 anos.
somaidade=0
mediaidade=0
maioridadeh=0
nomevelho=0
totmulher=0
for p in range(1,5):
    print(f'-______{p}° PESSOA ------')
    nome=str(input('qual o seu nome ?'))
    idade=int(input('qual a sua idade ?'))
    sexo=str(input(f'SEXO [M/F]:'))
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadeh=idade
        nomevelho=nome
    if sexo in 'Mm' and idade > maioridadeh:
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher+=1
mediaidade=somaidade/4
print(f' a media de idade do grupo e de {mediaidade} anos !')
print(f'O homem mas velho tem {maioridadeh} e se chama {nomevelho} !')
print(f' Ao todo são {totmulher} mulheres com menos de 20 anos !')