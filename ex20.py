from random import shuffle
n1=str(input('digite um nome'))
n2=str(input('digite um nome'))
n3=str(input('digite um nome'))
n4=str(input('digite um nome'))
lista=[n1,n2,n3,n4]
escolha=shuffle(lista)
print('A ordem sera !')
print(lista)