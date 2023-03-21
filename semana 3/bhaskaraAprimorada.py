#ax**2 + bx + c == 0
#a, b e c são valores de entrada pro nosso programa
#x1 == (-b + math.sqrt (b**2 - 4ac)) / 2a
#x2 == (-b - math.sqrt (b**2 - 4ac)) / 2a
#delta == (b**2 - 4ac)
#math.sqrt (ovalor) [para fazer a raiz quadrada de algo]
#se delta for igual a zero, a equação de segundo grau só terá uma raiz
#se delta for negativo, ela não terá raízes reais, só terá raízes imaginárias (print ('essa equação não possui raizes reais')
#se delta for maior do que zero, terão duas raízes

print ('olá, vamos fazer o cálculo de uma equação de segundo grau')

valorA = input ('digite o valor de a (lembrando que a é ax**2): ')
valorB = input ('digite o valor de b (lembrando que b é bx): ')
valorC = input ('digite o valor de c: ')

valorANum = float (valorA)
valorBNum = float (valorB)
valorCNum = float (valorC)

delta = (valorBNum**2 - 4 * valorANum * valorCNum)

#print ('o valor de delta é', delta)

if delta < 0:
    print ('esta equação não possui raízes reais')
else:
    import math
    
    x1 = (-1 * valorBNum + math.sqrt (delta)) / (2 * valorANum)
    #print ('o valor de x1 é', x1)
    
    x2 = (-1 * valorBNum - math.sqrt (delta)) / (2 * valorANum)
    #print ('o valor de x2 é', x2)

    if x1 != x2:
        if x1 < x2:
            y1 = x1
            y2 = x2
        else:
            y1 = x2
            y2 = x1
        print ('as raízes da equação são', y1, 'e', y2)
    else:
        print ('a raiz desta equação é', x1)

        


