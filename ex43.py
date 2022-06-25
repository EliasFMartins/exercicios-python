#desenvolva uma lógica que leia o peso e a altura  de uma pessoa caucule seu imc e mostre o seu status de acordo
#com a tabela abaixo:-abaixo de 18.5:baixo peso-entre 18.5 e 25 peso ideal-de 25 a 30 sobrepeso de 30 a 40 obesdade
#acima de 40 obesidade mórbida !
p=float(input('digite o seu peso !'))
a=float(input('digite a sua aultura !'))
imc= p/(a*a)
print(f'o seu imc e {imc}')
if imc<18.5:
    print(f' seu imc esta abaixo do peso !!')
elif 18.5<=imc<= 25:
    print(f'seu imc esta com peso ideal !!!')
    print(f'parabens !!!'.upper())
elif 25<=imc<= 30:
    print(f'seu IMC esta alto !!!')
    print(f'acomselhamos  a perda de peso para manter a saude !!'.upper())
else:
    print(f' o seu IMC esta muito alto !!!!')
    print(f'atenção e extritamente  recomedando perca de peso saude pode estar em risco !!!')