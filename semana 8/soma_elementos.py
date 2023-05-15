def soma_elementos (lista):
    #print ("entrou na função")
    tamanho_lista = len (lista)
    ultimo_indice = tamanho_lista - 1
    #print (ultimo_indice)

    controle = 0
    soma = 0
    while controle <= ultimo_indice:
        soma = soma + lista [controle]
        controle = controle + 1
    #print (soma)
    return soma

lista = []

numero = int (input ("digite números inteiros - quando quiser finalizar, digite 0: "))

while numero != 0:
    lista.append (numero)
    numero = int (input ("digite números inteiros - quando quiser finalizar, digite 0: "))

if numero == 0:
    soma_elementos (lista)
    
