numero = int (input ('digite um número para sabermos se há nele dois números adjacentes iguais: '))
adjacentesIguais = False
digitoAnterior = 0 #que valor eu coloco aqui? com o zero, se o número tem 0 ele já para de analisar no zero

#exemplo: 654
#exemploB: 655

while numero % 10 != 0 and not adjacentesIguais: #4
    digito = numero % 10 #4
    #print ('esse é o dígito:', digito) #4
    #digitoAnterior = digito #4 #isso aqui tava errado(está aqui para fins de registro)
    numero = numero // 10 #65
    if digitoAnterior == digito: #aqui tá dando errado, pois digitoAnterior e digito já foram igualados duas linhas acima (vou mudar isso!) #agora digitoAnterior vai ser 0 e digito vai ser 4 (vai rolar!)
        adjacentesIguais = True
    else:
        adjacentesIguais = False
    digitoAnterior = digito

if adjacentesIguais:
    print ('há nesse número números adjacentes iguais')
else:
    print ('não há nesse número números adjacentes iguais')
    
