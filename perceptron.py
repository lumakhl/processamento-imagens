import numpy as np

entrada = [[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
pesos = [0,0,0]
esperado = [0,0,1,1]

def limearizar(valor):
    return 1 if valor > 0 else 0
    
def transferencia(posicao, soma):
    print("input: {}, valor esperado: {}, Valor encontrado {}, Pesos {}".format(entrada[posicao],esperado[posicao], soma, pesos))
    if(esperado[posicao] != soma):
        if (soma == 0):
            for i in range(len(entrada[posicao])):
                pesos[i] = pesos[i] + entrada[posicao][i]
        else:
            for i in range(len(entrada[posicao])):
                pesos[i] = pesos[i] - entrada[posicao][i]
        return False
    return True

## Execucação do treinamento para calibrar os pesos
def treinamento():
    valido = False
    while(not(valido)):
        valido = True
        for i in range(len(entrada)):
            soma = 0
            for y in range(len(entrada[i])):
                soma += entrada[i][y] * pesos[y]

            soma = limearizar(soma)

            if not transferencia(i,soma):
                valido = False
            soma = 0

## Execucação da classificacao
def classificacao(items):
    
    classificacao = [None]*len(items)
    for i in range(len(items)):
        soma = 0
        for y in range(len(items[i])):
            soma += items[i][y] * pesos[y]
        
        soma = limearizar(soma)

        classificacao[i] = soma
    return classificacao

def exibir_resultados(input,resultado):
    for i in range(len(resultado)):
        resultado_final = limearizar(resultado[i])
        print("input: " + str(input[i]) + " Classe: "+ str(resultado_final))


def rede():
    treinamento()

    input = [[0,0,0],[0,0,1],[0,1,1],[0,1,0]]
    exibir_resultados(input,classificacao(input))

rede()
