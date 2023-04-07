def maximo (x, y, z):
    maior = 0
    if x > y:
        maior = x
    else:
        maior = y
    if maior < z:
        maior = z
    else:
        maior = maior

    return maior 
        
