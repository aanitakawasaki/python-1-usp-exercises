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



def n_primos (n):
    #vai passando de numeroDigitado até 2 (subtraindo de 1 em 1):
    numeroAtual = n
    quantidadePrimos = 0
    while numeroAtual >= 2:
        #vai verificando se cada um desses "numeroAtual" é primo
        if ePrimo (numeroAtual):
            quantidadePrimos = quantidadePrimos + 1    
        numeroAtual = numeroAtual - 1
        
    return quantidadePrimos
