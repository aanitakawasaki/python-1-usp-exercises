numero = int (input ('Digite um número inteiro: '))

numerosAdjacentesIguais = False
digitoAnterior = -1

while numero != 0 and not numerosAdjacentesIguais:
    digito = numero % 10
    #print (digito)
    if digito != digitoAnterior:
        numerosAdjacentesIguais = False
    else:
        numerosAdjacentesIguais = True
    numero = numero // 10
    digitoAnterior = digito

if numerosAdjacentesIguais:
    print ('sim')
else:
    print ('não')
    
