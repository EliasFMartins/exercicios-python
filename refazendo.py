'''n=int(input('digite hum numero inteiro , pra ver se o mesmo e INPAR ou PAR !'))
r= n % 2
if r == 0:
    print(f'o numero {n} e PAR !')
else:
    print(f'o numero {n} e INPAR !')'''
'''nc=str(input('digite o nome da sua cidade e veja se ela começa com al')).strip()
print(f'o nome da sua cidade e {nc}  e {nc[0:2].upper()=="AL"} começa  com Al !'.capitalize())'''
n=str(input('digite um nome veja se dentro do nome tem a letra e nele !')).strip()
print(f'o  nome digitado foi {n} e ele {"E"in n[:5].upper()} tem a letra E em sua composição!')
