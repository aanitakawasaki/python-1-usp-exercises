numero = int (input ('digite um número para sabermos se há nele dois números adjacentes iguais: '))
adjacentesIguais = False
#digitoAnterior = 0 #que valor eu coloco aqui? com o zero, se o número tem 0 ele já para de analisar no zero #o problema era isso e*¹
digitoAnterior = -1 #tentando com -1 (explicação:

#exemplo: 654
#exemploB: 655

#while numero % 10 != 0 and not adjacentesIguais: # # # #False and True (não é not something, portanto é true (?)) #*¹isso #pois se o número tinha 0 na última casa (unidade) ele já parava de analisar e já ia pro else 'não há nesse número números adjacentes iguais'
while numero != 0 and not adjacentesIguais: #(explicação:
    digito = numero % 10 #4 #5 #6
    #print ('esse é o dígito:', digito) #4 #5 #6
    #digitoAnterior = digito #4 #isso aqui tava errado(está aqui para fins de registro)
    numero = numero // 10 #65 #6 #0
    if digitoAnterior == digito: #aqui tá dando errado, pois digitoAnterior e digito já foram igualados duas linhas acima (vou mudar isso!) #agora digitoAnterior vai ser 0 e digito vai ser 4 (vai rolar!)
        adjacentesIguais = True
    else:
        adjacentesIguais = False #False #False #False
    digitoAnterior = digito #4 #5 #6

if adjacentesIguais:
    print ('há nesse número números adjacentes iguais')
else:
    print ('não há nesse número números adjacentes iguais')
    
