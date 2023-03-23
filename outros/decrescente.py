decrescente = True

anterior = int (input ("digite o primeiro número da sequência: "))

valor = 1

while valor !=0 and decrescente:
    valor = int (input ("digite o próximo número da sequência: "))
    if valor > anterior:
        decrescente = False
    anterior = valor

if decrescente:
    print ('a sequência está em ordem decrescente')
else:
    print ('a sequência não está em ordem decrescente')
