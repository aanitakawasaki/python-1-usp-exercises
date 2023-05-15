def remove_repetidos (lista):
    tamanho_lista = len (lista) #tamanho_lista = 4
    ultimo_indice = tamanho_lista - 1 #ultimo_indice = 3

    indice = 0 #0
    indice_b = indice + 1 #1
    while indice < ultimo_indice: #0 < 3 True #1 < 3 True 
        while indice_b <= ultimo_indice: #1 <= 3 True #2 <= 3 True #3 <= 3 True #3 <=4 False #2 <= 3 True #3 <= 3 True
            if lista [indice] != lista [indice_b]: #1 != 3 True #1 != 5 True #1 != 3 True #3 != 5 True #3 != 3 False
                indice_b = indice_b + 1 #2 #3 #4 #3
            else:
                print ('achou repetido:', lista [indice], 'é igual a', lista [indice_b])
        indice = indice + 1 #1
        indice_b = indice + 1 #2
        
lista = []

numero = int (input ("digite uma lista com números inteiros - para finalizar, digite 0: "))
while numero != 0:
    lista.append (numero)
    numero = int (input ("digite uma lista com números inteiros - para finalizar, digite 0: "))
#lista = 1, 3, 5, 3

if numero == 0:
    remove_repetidos (lista)    
