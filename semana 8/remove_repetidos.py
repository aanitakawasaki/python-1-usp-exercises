def remove_repetidos (lista):
    tamanho_lista = len (lista) #5
    ultimo_indice = tamanho_lista - 1 #4

    indice = 0 #0
    indice_b = indice + 1 #1
    while indice < ultimo_indice:
        while indice_b <= ultimo_indice:
            if lista [indice] != lista [indice_b]:
                indice_b = indice_b + 1
            else:
                del lista [indice_b]
                print (lista)
                ultimo_indice = ultimo_indice - 1
                
        indice = indice + 1
        indice_b = indice + 1 


        
lista = []

numero = int (input ("digite uma lista com números inteiros - para finalizar, digite 0: "))
while numero != 0:
    lista.append (numero)
    numero = int (input ("digite uma lista com números inteiros - para finalizar, digite 0: "))

if numero == 0:
    remove_repetidos (lista)    
    #lista = 1, 3, 5, 3, 5
