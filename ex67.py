#faça um programa que mostre uma taboada para cada numero digitado o programa deve ser interropido quando numero digitado for negativo !
while True:
    numero = int(input('digite um numero pra ver a sua taboada '))
    print('-' * 30)
    if numero < 0:
        break
    for c in range(1, 11):
         print(f' {numero}  X {c}  = {numero*c} !')
    print('-' * 30)
print('taboada encerrada , te vejo em breve !')