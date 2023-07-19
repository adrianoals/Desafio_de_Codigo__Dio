''' 
Desafio
Paulinho tem em suas mãos um novo problema. Agora a sua professora lhe pediu que construísse um programa para verificar, à partir de dois valores muito grandes A e B, se B corresponde aos últimos dígitos de A.

Entrada
A entrada consiste de vários casos de teste. A primeira linha de entrada contém um inteiro N que indica a quantidade de casos de teste. Cada caso de teste consiste de dois valores A e B maiores que zero, cada um deles podendo ter até 1000 dígitos.

Saída
Para cada caso de entrada imprima uma mensagem indicando se o segundo valor encaixa no primeiro valor, confome exemplo abaixo.

Verifique, para cada entrada A e B, se os dois valores são compatíveis e imprima se "encaixa" ou "não encaixa" para cada uma das relações N vezes.
'''

n = int(input('informe o número de testes: '))

while(n > 0):
    a = input('Informe o número A: ')
    b = input('informe o numero B: ')
    
    n -= 1

    if b[-3] == a[-3]:
        print('encaixa')
    else:
        print('não encaixa')
