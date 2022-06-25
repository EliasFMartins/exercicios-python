#melhore o exerçiçio anterior  perguntado quantos termos o usuario aiinda quer ver  , parando quando esse for igual a 0
print('Gerador de Pa')
term=int(input('digite o primeiro termo !'))
raz=int(input('digite a razão'))
print('=-='*20)
termo=term
pa=1
total=0
mais=10
while mais !=0:#foi adicionado mas uma condição de repetição !
    total=total+mais
    while pa<=total: #faz exibir as 10 repetições !
        print(f'{termo}',end=' ')#o numero inicial
        termo+=raz#o termo que começa valendo term+ a razão a cada repetição
        pa+=1#e responsavel pela contagem quando ele se iguala a 10  ele para
    print('pausa'.upper())#munda atenção com indentação
    mais=int(input(f'quantos termos vc quer mostar a mais ?'))#subistituir o valor de mais e mostra quantas repetições a mais o usuario ira querer !
print(f'a contagem de termos total foi de {pa} termos ')