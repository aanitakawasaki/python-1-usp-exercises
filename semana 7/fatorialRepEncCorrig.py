"""def fatorial (n):
    resultado = 1    
    while n >= 1:
        resultado = resultado * n
        n = n - 1
    return resultado"""

numeroDigitado = int (input ('digite um número inteiro positivo - um negativo para finalizar: '))
while numeroDigitado >= 0:
    fatorial = 1
    while numeroDigitado >= 1:
        fatorial = fatorial * numeroDigitado
        numeroDigitado = numeroDigitado - 1
    print ('o fatorial é', fatorial)
    numeroDigitado = int (input ('digite um número inteiro positivo - um negativo para finalizar: '))
