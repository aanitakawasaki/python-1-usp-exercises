def ePrimo (n):
    ePrimo = True
    divisor = n - 1
    while divisor > 1 and ePrimo:
        if n % divisor != 0:
            ePrimo = True
            divisor = divisor - 1
        else:
            ePrimo = False

    if ePrimo:
        return True
    else:
        return False



def verificaEPrimo (n):
    #vai passando de numeroDigitado até 2 (subtraindo de 1 em 1):
    numeroAtual = n
    quantidadePrimos = 0
    while numeroAtual >= 2:
        #vai verificando se cada um desses "numeroAtual" é primo
        if ePrimo (numeroAtual):
            return True
        else:
            return False

        numeroAtual = numeroAtual - 1
    #retorna a quantidade de números primos dentro daquele número:
    return quantidadePrimos



#recebe o número:
numeroDigitado = int (input ("digite um número maior ou igual a 2: "))
while numeroDigitado < 2:
    numeroDigitado = int (input ("digite um número maior ou igual a 2: "))
    verificaEPrimo (numeroDigitado)
    
#soma a quantidade de números primos
primos = 0
while verificaEPrimo (numeroDigitado):
    primos = primos + 1

print (primos)
    
