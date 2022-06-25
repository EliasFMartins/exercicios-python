#REFAÇA O DESAFIO  35  acrescentando 0 recurso de mostrar que tipo de triangulo sera formado :
#equilatero: todos os lados iguais -isósceles:dois lados iguais,-escaleno:todos os lados diferentes
d=float(input('digite o tamanho da primeira reta !!'))
d1=float(input('digiteo tamanho da segunda reta !!'))
d2=float(input('digite o tamanho da terceira reta!!!'))
if d<d1+d2 and d1<d+d2 and d2<d+d1:
    print(f' as retas acima podem forma um triangulo !!')
    if d==d1==d2:
      print('podem forma um triangulo equilatero ')
    elif d!=d1!=d2!=d:
      print('podem formar um triangulo escaleno !')
    else:
      print('podem forma um triangulo isociles !')
else:
    print('as retas acima não podem forma um triangulo !')