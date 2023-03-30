numeroN = int (input ('digite um número pra N: '))
numeroK = int (input ('digite um número maior ou igual a 0 pra K: '))

#exemplo: numeroN = 2   numeroK = 3

variavelControle = 1
multiplicando = 0
guardandoResultado = 1

while variavelControle <= numeroK: #True #True #True #False
    multiplicando = guardandoResultado * numeroN #2 #4 #8
    guardandoResultado = multiplicando #2 #4 #8
    numeroK = numeroK - 1 #2 #1 #0

print ('o resultado é:', guardandoResultado)
