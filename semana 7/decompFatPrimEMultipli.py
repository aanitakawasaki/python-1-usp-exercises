#to com preguiça de ficar fazendo esses exercícios matemáticos, vou fazer assistindo a solução
def decPrimos (n):
    fator = 2
    multiplicidade = 0

    while n > 1:
        while n % fator == 0:
            multiplicidade = multiplicidade + 1
            n = n / fator
        if multiplicidade > 0:
            print ("fator", fator, "tem multiplicidade:", multiplicidade)
        fator = fator + 1 #mas e quando o fator for 4, por exemplo, 4 não é um número primo! (ou isso acaba não sendo possível, isso: dividir um número por um número não primo, porque ele já foi dividido por 2 duas vezes - o que já substitui a divisão por 4. isso acontece sempre? talvez, né?)
        multiplicidade = 0

numeroDigitado = int (input ('digite um número inteiro > 1 - um negativo para finalizar: '))
while numeroDigitado >= 0:
    decPrimos (numeroDigitado)
    numeroDigitado = int (input ('digite um número inteiro > 1 - um negativo para finalizar: '))
    
