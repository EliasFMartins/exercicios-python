#refaça o desafio da taboada  mostrando  o numero da taboada mas agora utilizando o laço for!
n=int(input('digite um numero para ver a sua taboada !!!'))
for c in range(1,11):
    print(f'{n} X {c} = {n*c}')#o c se repete ate o 11 e o n e o numero que eu quero a taboada
    #logo fez se funcionar assim