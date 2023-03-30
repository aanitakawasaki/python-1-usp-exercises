numero = int (input ('Digite um número inteiro: '))

#exemplo: 9

numeroPrimo = True 
seiLa = numero - 1 

while seiLa != 1 and numeroPrimo:
    if numero % seiLa == 0:
        numeroPrimo = False
    else:
        numeroPrimo = True 
    seiLa = seiLa - 1
    #print (seiLa)

if numeroPrimo:
    print ('primo')
else:
    print ('não primo')
