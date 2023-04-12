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
            usuario_escolhe_jogada (n, m)

            while n != 0:
                computador_escolhe_jogada (n, m)
                usuario_escolhe_jogada (n, m)

            if n == 0:
                print ('Fim do jogo! Você ganhou!')
                
        else:
            print ('Computador começa!')
            computador_escolhe_jogada (n, m)

            while n != 0:
                usuario_escolhe_jogada (n, m)
                computador_escolhe_jogada (n, m)

            if n == 0:
                print ('Fim do jogo! O computador ganhou!')

    elif escolha == 2:
        campeonato ()



def computador_escolhe_jogada (n, m):

    nAntigo = n 
    controle = 1
    while n % (m + 1) != 0 and controle <= m:  
        n = nAntigo  
        n = n - controle 
        controle = controle + 1 

    pecasRetiradas = nAntigo - n

    print ('O computador tirou', pecasRetiradas, 'peça(s)')

    print ('Agora restam', n, 'peça(s) no tabuleiro.')

    return pecasRetiradas
    #o return só está aparecendo quando eu executo a função direto do terminal, colocando computador_escolhe_jogada (27, 3), por exemplo. é assim mesmo?
    #e se eu colocar o return aqui, ele para a função aqui e não vai para o if...else abaixo, né? como devo proceder, ein? coloquei aquele if...else lá pra cima (depois de chamar essa função)
    #mas jogando essa condição lá pra cima, eu vou ter que usar um while, pra ir alternando e não um if...else



def usuario_escolhe_jogada (n, m):

    nAntigo = n
    
    pecasRetiradas = int (input ('Quantas peças você vai tirar? '))
    while pecasRetiradas < 1 or pecasRetiradas > m:
        print ("Oops! Jogada inválida! Tente de novo.")
        pecasRetiradas = int (input ('Quantas peças você vai tirar? '))

    n = nAntigo - pecasRetiradas

    print ('Você tirou', pecasRetiradas, 'peça(s)')

    print ('Agora restam', n, 'peça(s) no tabuleiro.')

    return pecasRetiradas



def campeonato ():
    print ('Você escolheu um campeonato!')
    controle = 1
    while controle <= 3:
        print ('*** Rodada', controle, ' ***')
        
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
            usuario_escolhe_jogada (n, m)

            while n != 0:
                print ('Agora restam', n, 'peça(s) no tabuleiro.')
                computador_escolhe_jogada (n, m)
                usuario_escolhe_jogada (n, m)
                
            if n == 0:
                print ('Fim do jogo! Você ganhou!')
                
        else:
            print ('Computador começa!')
            computador_escolhe_jogada (n, m)

            while n != 0:
                print ('Agora restam', n, 'peça(s) no tabuleiro.')
                usuario_escolhe_jogada (n, m)
                computador_escolhe_jogada (n, m)

            if n == 0:
                print ('Fim do jogo! O computador ganhou!')


        controle = controle + 1

    print ('*** Final do campeonato! ***')

    #falta o "Placar: Você 0 X 3 Computador", mas como puxar esse número das funções computador_escolhe_jogada e usuario_escolhe_jogada sem sem por meio de um novo parâmetro?



partida ()
