def fatorial (n):
    fatorial = 1
    while n >= 1:
        fatorial = fatorial * n
        n = n - 1
    return fatorial

numeroDigitado = int (input ('digite um número inteiro positivo - um negativo para finalizar: '))
while numeroDigitado >= 0:
    fatorial (numeroDigitado)
    print ('o fatorial é', fatorial (numeroDigitado))
    numeroDigitado = int (input ('digite um número inteiro positivo - um negativo para finalizar: '))

