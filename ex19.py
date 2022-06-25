from random import choice
a1=str(input('digite o nome do aluno 01'))
a2=str(input('digite o nome do aluno 02'))
a3=str(input('digite o nome do aluno 03'))
a4=str(input('digite o nome do aluno 04'))
lista=[a1,a2,a3,a4]
escolhido=choice(lista)
print(f'O  alunos {a1} , {a2} ,{a3}, e {a4}, estão participando do \n'
      f'Sorteio , O Nome do Aluno sorteado foi {escolhido}!')
'''o choice e usado pra escolher uma  variavel dentro da lista a lista deve ser definida
pelos parametros dentro dos []  quero testar o choices'''