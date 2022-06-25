#escreva um programa q mostre a velocidade de um caro, se ele utrapassar 80km por hr recebera uma msg avisando que foi multado !
#sera multado em  7,00 por km acimda do limie
v=int(input('qual  e a sua  velicidade atual ? '))
lm=80
limite=(v-80)*7.00
vt=v-80
print(f' a sua velicidade atual e {v} e o limite de velicidade e {lm}')
if v<=lm:
    print('parabens vc esta dentro do limite de velocidade !')
else:
    print(f'voce ultrapasou o limite de velocidade de 80 km/h e sera multado\n'
          f'no valor de  {limite} Reais pela infrção de transito  !  !')