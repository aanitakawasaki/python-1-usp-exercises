#relembrando o conceito: uma hipotenusa é o lado maior de um triângulo retângulo (o lado oposto ao ângulo reto)
# hip² = catA² + catB² (sendo catA cateto A e catB cateto B)
# 10² = 6² + 8² (hip = 10; catA = 6; catB = 8)

def é_hipotenusa (n):
    #sendo n = 5
    catetoA = 1 #1
    while catetoA <= n: #1 <= 5 True #2 <= 5 True
        catetoB = 1 #1 #1
        while catetoB <= n: #1 <= 5 True #2 <= 5True [...] #True #False #True #True
            if catetoA ** 2 + catetoB ** 2 == n ** 2: #1 ** 2 + 1 ** 2 == 25 False #1 ** 2 + 2 ** 2 == 25 False #False #2 ** 2 + 1 ** 2 == 25 False #False
                #print (catetoA ** 2, "+", catetoB ** 2, "=", catetoA ** 2 + catetoB ** 2) 
                #print ("é a hipotenusa de algum triângulo retângulo com lados de comprimento inteiro")
                return True
            catetoB = catetoB + 1 #1 + 1 = 2 [...] #5 #6 #2 [...] PAREI AQUI
        catetoA = catetoA + 1 #1 + 1 = 2



def soma_hipotenusas (n):
    numeroAtual = 1
    soma = 0
    while numeroAtual <= n:
        if é_hipotenusa (numeroAtual):
            #print (numeroAtual)
            soma = soma + numeroAtual #era só fazer isso (que eu sempre faço) e colocar a variável soma pra fora desse if (pra não zerar toda vez que retomar a função)
        numeroAtual = numeroAtual + 1
    #print (soma)
    return soma



#numeroDigitado = (int (input ("digite um número inteiro positivo: ")))
#while numeroDigitado <= 0:
    #numeroDigitado = (int (input ("digite um número inteiro positivo: ")))

#soma_hipotenusas (numeroDigitado)
