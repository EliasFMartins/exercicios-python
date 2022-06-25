#faça um programa que peça o sexo de uma criaça mas so aceite  se a respostar foi m ou f  caso ao contrario continue repetindo !
v=str(input('digite o seu sexo :[ M ] ou [ F ] ?')).strip().upper()[0]# strip foi usado pra tirar os espaços ,upper desncessario e [0] foi pra tira a primeira letra
while v not in 'fFmM':#a condição foi enquanto v n for igual a fF mM vai mostra o input !
    v=str(input('f dados invalidos , por favor informe o seu sexo !')).strip().upper()[0]
print(f'sexo {v} resgitrado com sucesso !!!!')