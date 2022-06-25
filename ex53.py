#crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,desconsiderando os espaços.
#ex:apos a sopa
#ex 01
f=str(input('digite uma frase ')).upper().strip()
palavra=f.split()
junto=''.join(palavra)#o join serve pra juntar e o '' serve pra retirar os espaços !!!
inverso=''
for letra in range(len(junto)-1,-1,-1):# o len e pra pegar a ultima letra
    inverso+=junto[letra]
if inverso==junto:# serve pra comparar
        print(f'a {f}  e um polindromo !!!'.upper())
else:
        print(f'{f} , não temos um palindromo !!'.upper())

'''solução sem usar o for 
->inverso=junto[::-1] inverte a frase '''

""" frase = input("Qual a frase? ").upper().replace(" ", "")
if frase == frase[::-1]:
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")"""
#resolução mas simples  de um aluno !!!