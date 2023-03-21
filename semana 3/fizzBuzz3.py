numero = int (input ('digite um número inteiro: '))
if numero % 3 == 0:
    if numero % 5 == 0:
        print ('FizzBuzz')
    else:
        print (numero)
else:
    print (numero)
        
