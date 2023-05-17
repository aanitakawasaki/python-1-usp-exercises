def maior_elemento (lista):
    #print (lista) #[5, 7, 3, 2, 120]
    tamanho_lista = len (lista) #5
    ultimo_indice = tamanho_lista - 1 #4

    indice = 0 #0
    maior_elem = 0 #0
    while indice <= ultimo_indice: #0 <= 4 True #1 <= 4 True #2 <= 4 True # 3 <= 4 True #4 <= 4 True #5 <= 4 False
        if maior_elem < lista [indice]: #0 < 5 True #5 < 7 True #7 < 3 False #7 < 2 False #7 < 120 True
            maior_elem = lista [indice] #5 #7 #120
        else:
            maior_elem = maior_elem #7 #7
            
        indice = indice + 1 #1 #2 #3 #4 #5

    #print (maior_elem)
    return maior_elem



lista = []
numero = int (input ("escreva uma lista com números inteiros - para finalizar digite 0: "))

while numero != 0:
    lista.append (numero)
    numero = int (input ("escreva uma lista com números inteiros - para finalizar digite 0: "))

if numero == 0:
    maior_elemento (lista)
