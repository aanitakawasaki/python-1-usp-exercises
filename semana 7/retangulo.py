largura = int (input ('digite a largura: '))
altura = int (input ('digite a altura: '))

printandoAltura = 1
while printandoAltura <= altura:
    printandoLargura = 1
    while printandoLargura <= largura:
        print ('#', end = '')
        printandoLargura = printandoLargura + 1
    print (' ')
    printandoAltura = printandoAltura + 1


