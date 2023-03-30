numero = int (input ('digite um número para sabermos se há nele dois números adjacentes iguais: '))
adjacentesIguais = False
digitoAnterior = -1 

while numero != 0 and not adjacentesIguais:
    digito = numero % 10
    numero = numero // 10 
    if digitoAnterior == digito:
        adjacentesIguais = True
    else:
        adjacentesIguais = False 
    digitoAnterior = digito 

if adjacentesIguais:
    print ('há nesse número números adjacentes iguais')
else:
    print ('não há nesse número números adjacentes iguais')
    

