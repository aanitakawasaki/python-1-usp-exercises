def ePrimo (n):
#testando: n = 9
    divisor = 2 #3
    while n % divisor != 0 and divisor != n: #9 % 2 != 0 True and True #9 % 3 != 0 False and True
        divisor = divisor + 1
        
    if divisor != 1 and divisor != n: #isso poderia ser: if n % divisor == 0:
        return False
    else:
        return True

numero = int (input ("digite um número inteiro maior do que zero: "))

while numero > 0:
    if numero == 2:
        print (numero, "é primo")
    else:
        if ePrimo (numero):
            print (numero, "é primo")
        else:
            print (numero, "não é primo")
        
    numero = int (input ("digite um número inteiro maior do que zero: "))

