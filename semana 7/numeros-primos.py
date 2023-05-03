numero = int (input ("digite um número inteiro maior do que zero - um menor do que zero para finalizar: "))

def ePrimo (n):
    numeroPrimo = True
    divisor = numero - 1

    while divisor != 1 and numeroPrimo:
        if numero % divisor == 0:
            numeroPrimo = False
        else:
            numeroPrimo = True
        divisor = divisor - 1

    if numeroPrimo:
        print ("primo")
    else:
        print ("não primo")

while numero > 0:
    ePrimo (numero)
    numero = int (input ("digite um número inteiro maior do que zero - um menor do que zero para finalizar: "))

#onde eu encaixo isso, ein?:
    #if numero == 1:
    #print ("não primo")
