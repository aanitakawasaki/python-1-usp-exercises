numero = int (input ('Digite um número inteiro: '))

somaAnterior = 0
digito = 0
soma = 0

#testando: 253

while numero != 0:
    digito = numero % 10
    #print (digito)
    soma = somaAnterior + digito
    #print (soma)
    numero = numero // 10 
    somaAnterior = soma #somaAnterior passa a ser 'soma' e não 'digito'

print (soma)
