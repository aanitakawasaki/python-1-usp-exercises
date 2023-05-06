#relembrando o conceito: uma hipotenusa é o lado maior de um triângulo retângulo (o lado oposto ao ângulo reto)
# hip² = catA² + catB² (sendo catA cateto A e catB cateto B)
# 10² = 6² + 8² (hip = 10; catA = 6; catB = 8)

def é_hipotenusa (n):
    catetoA = 1
    while catetoA <= n: 
        catetoB = 1 
        while catetoB <= n: 
            if catetoA ** 2 + catetoB ** 2 == n ** 2:
                print (catetoA ** 2, "+", catetoB ** 2, "=", catetoA ** 2 + catetoB ** 2)
                print ("hipotenusa")
            catetoB = catetoB + 1 
        catetoA = catetoA + 1 

#def soma_hipotenusas (n):


    
numeroDigitado = (int (input ("digite um número inteiro positivo: ")))
while numeroDigitado <= 0:
    numeroDigitado = (int (input ("digite um número inteiro positivo: ")))

é_hipotenusa (numeroDigitado)
