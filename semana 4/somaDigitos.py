numero = int (input ("digite um número para que possamos somar os seus dígitos: "))
digitoDaVez = 0
soma = 0

#exemplo: numero = 654

while numero % 10 != 0: #4 prossegue #5 prossegue #6 prossegue #0 não prossegue #isso significa: enquanto o resto da divisão do número por 10 for diferente de 0 (e?)
    digito = numero % 10 #4 #5 #6
    #print ('dígito:', digito) #4 #5 #6
    #digito = digito + digito #isso aqui tá errado (está aqui para fins de registro), porque ele pega o mesmo dígito, preciso dar um jeito de ele pegar o dígito da rodada anterior (na verdade a soma da rodada anterior) e o da rodada atual
    digitoDaVez = digito #aqui transformo o digito em digitoDaVez (da rodada)
    soma = soma + digitoDaVez #aqui somo a soma anterior ao dígito da vez
    numero = numero // 10 #65 #6 #0
    
print ('a soma dá:', soma)
