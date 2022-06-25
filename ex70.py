#crie um programa que leia o nome o preço de varios produtos e ao final diga  se ele quer continuar  quanto foi gasto qual o numero de produtos que
#custao mas de 1000 reais
#e qual produto foi mas barato !
soma=maiorq=cont=menor=0
baratp=''
while True:
    produto=str(input('digite o nome do produto que vc deseja comprar '))
    valor=float(input('digite o valor do produto !'))
    cont += 1
    soma+=valor
    if cont==1 or valor<menor:# vai pega o primeiro valor ou or quer dizer ou
        baratp=produto
        menor=valor#se tiver so um numero inserido ele vai pegar o numero
        valor=menor
    elif valor >=1000:
        maiorq+=1

    resp = ' '#sempre colocar espaço se n n vai
    while resp not in 'SN':
        resp = str(input('quer continuar [ S ]/[ N ]')).upper().strip()[0]
    if resp== 'N':
            break
print(f'o total gasto em compras foi R${soma}')
print(f'o produto mais barato foi{baratp}que custa {menor}')
print(f'a quantidade de produtos acima de 100 foi {maiorq} ')

