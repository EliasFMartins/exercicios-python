# escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual sera a
#base de conversão  :
#-1 para binario
#-2para octal
#-3 para hexadecimal
n=int(input('digite um numero inteiro qualquer e escolha a base de conversão!'))
print('''escolha uma base para conversão !
[-1] PARA BINARIO 
[-2]PARA OCTAL
[-3] PARA HEXADECIMAL''')
op=int(input('digite a sua opção'))
if op==1:
    print(f'o numero {n} convertido para binario e {bin(n)[2:]} !')
elif op==2:
    print(f'o numero {n} convertido para octal  e {oct(n)[2:]} !')
elif op==3:
    print(f'o numero {n}  convertido para hexadecimal e {hex(n)[2:]} !')#lenbrar  da fatiação os couchetes demarcão a contagem
else:
    print('opção invalida !!! tente novamente !!'.upper())