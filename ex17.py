'''co=float(input('digite o comprimento  do cateto oposto !'))
ca=float(input('digite o comprimento  do cateto adjacente !'))
print(f'o valor do cateto oposto e  {co} e o valor do cateto adjacente e {ca} sendo\n'
      f'assim o valor da hipotenusa e {(co**2+ca**2)**(1/2):.2f} '''
from math import hypot
co=float(input('digite o comprimento  do cateto oposto !'))
ca=float(input('digite o comprimento  do cateto adjacente !'))
hy=hypot(co,ca)
print(f'o valor da hypotenusa e {hy:.2f} !')

'''obs: o primeiro metodo foi feito usando operação matematica , ja o segundo foi feito improtando
a função da biblioteca '''
