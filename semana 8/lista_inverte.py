numeros = []
numero = int (input ("digite uma sequencia de números inteiros terminados por 0 e quando quiser finalizar e inverter a lista, digite 0: "))
numeros.append (numero)
while numero > 0:
    numero = int (input ("digite uma sequencia de números inteiros terminados por 0 e quando quiser finalizar e inverter a lista, digite 0: "))
    if numero > 0:
        numeros.append (numero)
    else:
        indice = len (numeros) - 1
        while indice >= 0:
            print (numeros [indice])
            indice = indice - 1
            
