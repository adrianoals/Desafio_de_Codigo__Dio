#DESAFIO
"""
O microblog Twitter é conhecido por limitar as postagens em 140 caracteres. Conferir se um texto vai caber em um tuíte é sua tarefa.

T = input()
     
Ler a variável de entrada e verificar se ela possui mais ou menos que 140 caracteres.
Se for maior imprima "MUTE" e se for igual ou menor imprima "TWEET".    
"""

t = input('Digite seu Tweet \n')

if len(t) > 140:
    print('MUTE')
else:
    print('TWEET')
