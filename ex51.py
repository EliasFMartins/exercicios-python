#desenvolva um programa que leia o primeiro termo e a razão de uma PA no final mostre os 10 primeiros termos
#dessa progressão !
primeiro=int(input('digite o primeiro termo !'))
razão=int(input('digite o  razão da progressão !!'))
decimo=primeiro+(10-1)*razão#feito usando formula matematica  !!!
for c in range(primeiro,decimo+razão,razão):#primeiro  e onde começa , decimo e a razão e pra cauicular o fim
    # e a razão e a razão literalemte
    print(f'{c}',end='->')
print('the end !!!')
