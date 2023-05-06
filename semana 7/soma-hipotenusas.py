#relembrando o conceito: uma hipotenusa é o lado maior de um triângulo retângulo (o lado oposto ao ângulo reto)
# hip² = catA² + catB² (sendo catA cateto A e catB cateto B)
# 10² = 6² + 8² (hip = 10; catA = 6; catB = 8)

def é_hipotenusa (n):
    #sendo n = 1 #sendo n = 2
    catetoA = n #1 #2
    while catetoA <= n: #True #False
        catetoB = 1 #1
        while catetoB <= n: #True #False
            print (catetoA ** 2, "+", catetoB ** 2, "=", catetoA **2 + catetoB ** 2) #1**2 + 1**2 = 2
            catetoB = catetoB + 1 #2
        catetoA = catetoA + 1 #2

#def soma_hipotenusas (n):


    
numeroDigitado = (int (input ("digite um número inteiro positivo: ")))
while numeroDigitado <= 0:
    numeroDigitado = (int (input ("digite um número inteiro positivo: ")))
    #sendo numeroDigitado = 10

numeroAtual = 1 #1
while numeroAtual <= numeroDigitado: #1 <= 10 True #2 <= 10 True
    é_hipotenusa (numeroAtual) #é_hipotenusa (1) #é_hipotenusa (2)
    numeroAtual = numeroAtual + 1 #numeroAtual = 1 + 1 = 2
