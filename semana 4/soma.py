print ('digite uma sequencia de valores a ser somados. quando quiser saber o resultado final, digite 0 (zero)')

soma = 0
valor = 1

while valor != 0:
    valor = int (input ('digite um valor a ser somado: '))
    soma = soma + valor
    
print ('o resultado final é:', soma)
