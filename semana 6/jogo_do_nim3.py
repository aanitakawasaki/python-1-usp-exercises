def partida ():
    print ('Bem-vindo ao jogo do NIM! Escolha:')

    print ('1 - para jogar uma partida isolada')
    print ('2 - para jogar um campeonato')

    escolha = int (input ('digite: '))

    if escolha == 1:
        print ('Você escolheu uma partida isolada!')

        n = int (input ("Quantas peças? "))
        while n < 1:
            print ("Você deve colocar no mínimo 1 peça no tabuleiro!")
            n = int (input ("Quantas peças? "))

        m = int (input ("Limite de peças por jogada? "))
        while m < 1 or m > n:
            print ("Você deve permitir a retirada de pelo menos 1 peça do tabuleiro. E não pode permitir a retirada de mais peças do que a quantidade total no tabuleiro")
            m = int (input ("Limite de peças por jogada? "))

    if n % (m + 1) == 0:
        print ('Você começa!')
        
        while n != 0:
            '''aqui eu não preciso chamar a função usuario_escolhe_jogada (n, m) e depois atribuir
            usuario_escolhe_jogada (n, m) à pecasRetiradas, como eu estava fazendo, só fazer essa atribuição,
            como abaixo, já basta, afinal*'''
            pecasRetiradas = usuario_escolhe_jogada (n, m)
            print ('Você tirou', pecasRetiradas, 'peça(s)')
            n = n - pecasRetiradas
            print ('Agora restam', n, 'peça(s) no tabuleiro')
            usuario_joga = False

            pecasRetiradas = computador_escolhe_jogada (n, m)
            print ('O computador retirou', pecasRetiradas, 'peça(s)')
            n = n - pecasRetiradas
            print ('Agora restam', n, 'peça(s) no tabuleiro')
            usuario_joga = True

        if n == 0 and usuario_joga:
            print ('Fim do jogo! o computador ganhou!')

    else:
        print ('Computador começa!')



def usuario_escolhe_jogada (n, m):
    pecasRetiradas = int (input ('Quantas peças você vai tirar? '))
    
    while pecasRetiradas < 1 or pecasRetiradas > m:
        print ("Oops! Jogada inválida! Tente de novo.")
        pecasRetiradas = int (input ('Quantas peças você vai tirar? '))
    
    return pecasRetiradas



def computador_escolhe_jogada (n, m):

    nAntigo = n 
    controle = 1
    while n % (m + 1) != 0 and controle <= m:  
        n = nAntigo  
        n = n - controle 
        controle = controle + 1 

    pecasRetiradas = nAntigo - n

    return pecasRetiradas



partida ()



'''
O erro está em partes do seu código que são assim:
    usuario_escolhe_jogada (n, m)
    n = n - (usuario_escolhe_jogada (n, m))
Uma função não é uma variável: toda vez que você chama ela, o código inteiro dentro dela é executado. Nesse caso
acima você chama a função com valores n e m, e não guarda seu retorno em nenhum lugar. Em baixo você chama de novo
mas ai você usa o valor de retorno da função.
'''
