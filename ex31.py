#desenvolva um programa q pergunte a distancia da viagem em km  caucule o preço da viagem cobrando 0,50cnts ate 200 km
# e 45 cnts  acima de  200 km por quilometro rodado  e caucule o preço da pasagem !
import math
d=int(input('qual a  distancia da viagem desejada  em Km ?'.title()))
if d<=80:
    print(f'a distancia e de 80 km ou inferior portanto vc pagara 50 cnts por km\n'
          f'portanto o valor da viagem sera {d*0.50}  reais !'.capitalize())
else:
    print(f'a distancia e superior a 80 km portanto vc pagar uma tarifa reduzira de 45 cnts por km\n'
          f'portanto o valor da viagem sera de {d*0.45} reais !'.capitalize())
    print('agradecemos a preferencia !'.upper())
#forma simplificada
#preco=d*0.50 if d<=200 e else d*045
#apena em uma linha