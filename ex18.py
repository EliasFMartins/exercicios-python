from math import radians,sin,cos,tan
ag=float(input('digite um algulo parar caucular o seno cosseno e  tangente !'))
se=sin(radians(ag))
cos=cos(radians(ag))
tan=tan(radians(ag))
print(f' o valor do angulo e {ag} , o valor do seno e {se:.2f} i valor do cosseno e {cos:.2f} \n '
      f'e o valor  da tangent e {tan:.2f} ! ')
'''e necessario usar o radians para converter o angulo em todas as funçoes cauculadas !'''
