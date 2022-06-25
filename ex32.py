#faca um programa q leia um ano qualquer e mostre se ele e bicesto ou nao !
from datetime import date
a=int(input('digite o ano que vc naceu que o computador lhe dira se e bicesto ou nao e 0 para o ano atual !'.title()))
if a==0:#colocado como outra opção !!
    a=date.today().year#essa função importa a data atual do sistema !
if a % 4==0 and a % 100 != 0 or a % 400 ==0:
    print(f'O ano {a} e bissexto !')
else:
    print(f'o ano {a} não e bissexto !')