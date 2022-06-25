# a comfederação macopmaç de matação  precisa de uim programa que leia o ano de nsacimento de um atleta e
#mostre a sua categoria de agordo com a idade:
#ate9 anos mirim ate 14 anos infantil ate 19 jinior ate 20 senior acioma master
ano=int(input('digite o ano de nascimento do nadador !'))
from datetime import date
att=date.today().year
idade=att-ano
if idade<=9:
    print(f'vc tem {idade}  anos e  considerado um nadador  mirin !'.upper())
elif idade<=14:
    print(f'vc tem {idade}  anos e considerado um nadador junior  !'.upper())
elif idade<=19:
    print(f'vc tem {idade}  anos e considerado um nadador Senior !'.upper())
elif idade>=20:
    print(f'vc  tem {idade} anos e considerado um nadador master !'.upper())