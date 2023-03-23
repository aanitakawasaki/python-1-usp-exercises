valores = int (input ('digite uma sequencia de valores a ser somados. mas antes, digite o número de valores que será somado: '))

soma = 0
iniciadorSeiLa = 1

while iniciadorSeiLa <= valores:
    valor = int (input ('digite um valor a ser somado: '))
    soma = soma + valor
    iniciadorSeiLa = iniciadorSeiLa + 1
    
print ('o resultado final é:', soma)
