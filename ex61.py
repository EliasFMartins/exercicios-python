#refaça o exercicio 51 lendo o primeiro termo e a razão  de uma pa  mostrando os 10 primeiros termos da progresão usando a while
print('Gerador de Pa')
term=int(input('digite o primeiro termo !'))
raz=int(input('digite a razão'))
print('=-='*20)
termo=term
pa=1
while pa<=10:#faz exibir as 10 repetições !
    print(f'{termo}',end=' ')#o numero inicial
    termo+=raz#o termo que começa valendo term+ a razão a cada repetição
    pa+=1#e responsavel pela contagem quando ele se iguala a 10  ele para
print('fim !')