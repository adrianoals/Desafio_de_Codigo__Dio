#Resolução Chat GPT

def verifica_encaixe(A, B):
    if len(B) > len(A):
        return "nao encaixa"
    
    if A[-len(B):] == B:
        return "encaixa"
    else:
        return "nao encaixa"

# Função para ler os valores de entrada
def ler_valores():
    N = int(input())  # Quantidade de casos de teste
    casos_teste = []
    for _ in range(N):
        A, B = input().split()
        casos_teste.append((A, B))
    return casos_teste

# Função para resolver os casos de teste e imprimir os resultados
def resolver_desafio(casos_teste):
    for caso in casos_teste:
        resultado = verifica_encaixe(caso[0], caso[1])
        print(resultado)

# Executar o programa
casos_teste = ler_valores()
resolver_desafio(casos_teste)

'''
Esse código define uma função verifica_encaixe que recebe duas strings A e B e verifica se B corresponde aos últimos dígitos de A. A função ler_valores lê os valores de entrada e retorna uma lista de casos de teste. A função resolver_desafio recebe essa lista de casos de teste, chama a função verifica_encaixe para cada caso e imprime o resultado.

Basta executar o programa para resolver o desafio. Ele solicitará a entrada de acordo com as especificações do problema e, em seguida, imprimirá os resultados para cada caso de teste.
'''