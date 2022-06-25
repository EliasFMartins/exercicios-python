#crie um programa que leia o ano de nascimento de sete pessoas.no final,mostre quantas pessoas ainda não  atingiram
#a maioridade e quantas já são maiores.
from datetime import date#biblioteca responsavel por puxar o ano atual !
totalm = 0#variavel utilizada para gravar a quantidade de  maiores de idade !
totalmn = 0#variavel utilizada pra gravar a quantidade de usuarios menores de idade !
atual=date.today().year
for pess in range(1,7):#usei do 1 ao 7 pq a ultima e descartada por isso geralmente começa no 0
    data=int(input('digite o seu ano de nascimento !'))
    idad=atual-data
    if idad<21:
        totalmn+=1
    else:
        totalm+=1
print(f' o total de pessoas maiores de idade são {totalm} !')
print(f' o total de pessoas menores de idade e {totalmn} !')