print ('olá, vamos fazer o cálculo de uma equação de segundo grau')

valorA = float (input ('digite o valor de a (lembrando que a é ax**2): '))
valorB = float (input ('digite o valor de b (lembrando que b é bx): '))
valorC = float (input ('digite o valor de c: '))

delta = (valorB**2 - 4 * valorA * valorC)

if delta < 0:
    print ('essa equação não possui raizes reais')
else:
    import math
    
    x1 = (-1 * valorB + math.sqrt (delta)) / (2 * valorA)
    
    x2 = (-1 * valorB - math.sqrt (delta)) / (2 * valorA)

    if x1 != x2:
        print ('a primeira raiz é', x1, 'e a segunda raiz é', x2)
    else:
        print ('o valor da primeira e da segunda raiz são iguais, ambos são:', x1)



#COMO APLICAR FUNÇÕES (PARA SIMPLIFICAR O CÓDIGO) AQUI?
