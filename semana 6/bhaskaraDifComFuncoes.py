print ('olá, vamos fazer o cálculo de uma equação de segundo grau')

import math

def delta (a, b, c):
    return b**2 - 4 * a * c

"""def main ():
    a_digitado = float (input ('digite o valor de a: '))
    b_digitado = float (input ('digite o valor de b: '))
    c_digitado = float (input ('digite o valor de c: '))
    imprime_raizes (a_digitado, b_digitado, c_digitado)"""
#porque assim não chama o input automaticamente e não guarda os valores de a, b e c pro código inteiro. acho que assim dará certo*¹:
a_digitado = float (input ('digite o valor de a: '))
b_digitado = float (input ('digite o valor de b: '))
c_digitado = float (input ('digite o valor de c: '))

def imprime_raizes (a, b, c):
    d = delta (a, b, c)
    if d < 0:
        print ('essa equação não possui raizes reais')
    else:
        x1 = (-1 * b + math.sqrt (d)) / (2 * a)
    
        x2 = (-1 * b - math.sqrt (d)) / (2 * a)

        if x1 != x2:
            print ('a primeira raiz é', x1, 'e a segunda raiz é', x2)
        else:
            print ('o valor da primeira e da segunda raiz são iguais, ambos são:', x1)

#*¹preciso chamar a imprime_raizes com os parâmetros aqui também:
imprime_raizes (a_digitado, b_digitado, c_digitado)



#testar com a: 3, b: -15, c: 12 (respostas 1 e 4)
#testar com a: 9, b: -24, c: 16 (resposta 4/3)
#testar com a: 1, b: -2, c: 4 (resposta: não possui raizes reais)
