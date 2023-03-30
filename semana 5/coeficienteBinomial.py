def fatorial (numero):
    controlePosicao = 0
    resultadoConta = 1 #se eu deixasse resultadoConta = numero, o fatorial de 0 daria errado (daria 0)
    #testando com: numero = 4
    while controlePosicao < numero and (numero - 1) != 0: #True #True #True #False
        resultadoConta = resultadoConta * numero #12 #24 #24 #se eu deixasse resultadoConta * (numero - 1), daria errado (daria sempre o fatorial de um número abaixo)
        numero = numero - 1 #3 #2 #1
    return resultadoConta #24
#um jeito muito mais simples de fazer essa função (que o professor ensinou):
def fatorialAprimorado (n):
    fat = 1
    while (n > 1):
        fat = fat * n
        n = n-1
    return fat

def numeroBinomial (n, k):
    resultadoFinal = fatorial (n) / (fatorial (k) * fatorial (n-k))
    return resultadoFinal
#não entendi o que é coeficiente/número binomial, portanto não consigo escrever a função de teste automatizada para essa função (numeroBinomial) rs
