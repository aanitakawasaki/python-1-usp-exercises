largura = int (input ('digite a largura: '))
altura = int (input ('digite a altura: '))

#testando:
#largura = 4
#altura = 3 

printandoAltura = 1 #1
if printandoAltura == 1: #True
    printandoLargura = 1 #1
    while printandoLargura <= largura: # 1 <= 4 True #True #True #True #False
        print ('#', end = '') #***
        printandoLargura = printandoLargura + 1 #2 #3 #4 #5
    print ('',end = '\n') #vai pra linha debaixo
    printandoAltura = printandoAltura + 1 #2 

while printandoAltura < altura: #2 < 3 True
    printandoLargura = 1 #1
    while printandoLargura <= largura: #1 <= 4 True #3 <= 4 True #5 <= 4 False
        if printandoLargura == 1: #1 == 1 True #False
            print ('#', end = '') #***
            printandoLargura = printandoLargura + 1 #2
        if printandoLargura < largura: #2 < 4 True #3 < 4 True
            print ('', end = ' ') #***
            printandoLargura = printandoLargura + 1 #3 #4
        if printandoLargura == largura: #False # 4 == 4 True
            print ('#', end = '')#***
            printandoLargura = printandoLargura + 1 #5
    print ('',end = '\n') #vai pra linha debaixo
    printandoAltura = printandoAltura + 1 #3

if printandoAltura == altura: #3 == 3 True
    printandoLargura = 1 #1
    while printandoLargura <= largura: #1 <= 4 True #True #True #True #False
        print ('#', end = '') #***
        printandoLargura = printandoLargura + 1 #2 #3 #4 #5 
    print ('',end = '\n') #vai pra linha debaixo



#***:
####
#  #
####


