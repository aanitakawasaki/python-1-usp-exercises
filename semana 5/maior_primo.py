def ePrimo (numero):
    controlePosicao = numero - 1
    numeroPrimo = True

    if numero == 1:
        #print ('não é número primo')
        return 'não primo'
    else:
        while controlePosicao != 1 and numeroPrimo:

            if numero % controlePosicao == 0:
                numeroPrimo = False
            else:
                numeroPrimo = True

            controlePosicao = controlePosicao - 1

        if numeroPrimo:
            #print ('número primo')
            return 'primo'
        else:
            #print ('não é número primo')
            return 'não primo'

def maior_primo (numeroRecebido):
    
    while numeroRecebido != 0 and ePrimo (numeroRecebido) == 'não primo': #aqui tava faltando eu completar a função com o parâmetro, assim: ePrimo (numeroRecebido) == 'não primo'
        #ePrimo (numeroRecebido) #como eu chamei a função lá em cima, eu nem preciso disso (acho que nem daria certo também)
        numeroRecebido = numeroRecebido - 1

    #if ePrimo == 'primo': #não precisa disso. só o return quando, no laço acima, identificarem um número primo, já é suficiente
    return (numeroRecebido)
    
