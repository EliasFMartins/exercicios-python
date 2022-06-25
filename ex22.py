n=str(input('digite o seu nome completo !'.title())).strip()
ns=n.strip('')
print(f'o seu nome e {n} !')
print(f'o seu nome com todas as letras Maiusculas e {"="*5, n.upper(),"="*5} !')
print(f'o seu nome com todas as letras minisculas e {"="*5, n.lower(),"="*5} !')
print(f"o Seu nome tem {len(n)-n.count(' ')} letras.")
#print(f"o seu primeiro nome tem {n.find(' ')} letras")
#a função .count serve pra contar os espaços  logo e so subitrar  pra saber o valor real
#colocar (' ') e preciso colocar 2  aspas
SS=n.split()
print(f'o primeiro nome e {SS[0]} e  tem {len(SS[0])} letras!')


#cara de longe o Desafio mas dificil que ja resolvi demonadou muito tempo e esforço ...
# aprendi algumas coisas muito uteis uma delas e as "" duplas
#segundo .split separa a frase , e o len le a quantidade de  letras da frase selecioada.


