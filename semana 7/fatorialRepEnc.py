#receber sequencia de números
#imprimir fatorial de cada um desses números (na medida em que eles vão sendo digitados (um número, um fatorial, um número, um fatorial e assim por diante)?

def fatorial (n):
    resultado = 1
    if n == -1:
        print ('fim')
    else:
        while n >= 1:
            resultado = resultado * n
            n = n - 1
        return resultado

numeroDigitado = int (input ('digite um número - para finalizar digite -1 (menos um): '))
print ('o fatorial de', numeroDigitado, 'é', fatorial (numeroDigitado))
     
while numeroDigitado != -1:
        numeroDigitado = int (input ('digite um número - para finalizar digite -1 (menos um): '))
        print ('o fatorial de', numeroDigitado, 'é', fatorial (numeroDigitado))

#no final aparece um 'o fatorial de -1 é None', quando digito -1 para finalizar (finaliza, mas aparece isso depois do 'fim')
