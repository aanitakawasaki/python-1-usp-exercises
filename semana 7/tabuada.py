linha = 1
coluna = 1

while linha <= 10:
    while coluna <= 10:
        print (linha * coluna, end = "\t") #\t separa com tab (faz o cursor avançar para a próxima coluna de tabulação
        coluna = coluna + 1
    coluna = 1
    print (" ") #pra separar as linhas das tabuadas de cada número
    linha = linha + 1
     
