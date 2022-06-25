f=str(input('Digite uma Frase Para Ser Analisada !')).strip()#sempre colocar strip pra tirar espaços na hora de caucular !
print(f' A Frase aparece {f.upper().count("A")}  vezes na frase ')#a função count conta a quantidade de variaveis na frase
print(f'a primeira lentra A apareceu {f.find("A")+1}')#a função find procura a primeira letra do lado direito !
print(f'a ultima vez q a letra A apareceu foi {f.rfind("A")+1}')# a função rfind procura a letra pelo lado oposto !




