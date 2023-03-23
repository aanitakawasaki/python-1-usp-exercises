valores = int (input ('digite uma sequencia de valores a ser multiplicados. antes, defina quantos valores serão multiplicados: '))

produto = 1 #o valor neutro pra iniciar multiplicação é 1 e não 0
iniciadorSeiLa = 1

while iniciadorSeiLa <= valores:
    valor = int (input ('digite um valor a ser multiplicado: '))
    produto = produto * valor
    iniciadorSeiLa = iniciadorSeiLa + 1
    
print ('o resultado final é:', produto)
