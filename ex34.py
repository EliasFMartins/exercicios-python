#faça um programa que leia e caucule o salario de um funcionario  aqueles que ganhao acima de 1250 tem  um almento de  10%
#aqueles q ganham menor ou igual de 1250 tem um almento de 15%
s=float(input('digite o valor do seu salario e lhe direi o valor apos o reajuste  !'.title()))
salario = float(input('digite o seu salario pra ver o reajuste !'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:                                      #essa foi a forma do guanabara a de baixo foi a minha !
    novo = salario + (salario * 10 / 100)
print(f'salario era {salario:.2f}  e foi para {novo:.2f}')

'''  if s > 1250:
         print(f'o Seu salario de {s} e maior a 1250.00 portanto tera um reajuste de 10%\n'
     f'subindo assim para {(s * 10) / 100 + s}  !'.capitalize())
     else:
     print(f'o seu salario e {s}  e inferior a 1250.00 ´portanto tera um reajuste de 15%\n'
     f'subindo assim para {(s * 15) / 100 + s}  !'.capitalize())
      #versão do guanabara'''