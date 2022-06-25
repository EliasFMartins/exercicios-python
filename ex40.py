#crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uima msg no final , de acordo
#com a media atingida: media abaixo de 5.0 reprovado media de 5.0 a 6.9 recperação media de 7.0 ou superior aprovado
n1=float(input('digite a primeira nota !'))
n2=float(input('digite a segunda nota !'))
m=(n1+n2)/ 2
if m >= 7.0:
    print(f'a media das 2 notas foi {m} !')
    print('parabens vc foi aprovado !!!'.upper())
elif m>= 5.0:
    print(f' a sua media foi de {m} !')
    print(f' vc ficou de recuperação !!!'.upper())
else:
    print(f'a sua media foi de {m} !!')
    print(f'infelizmente vc foi reprovado !!!'.upper())