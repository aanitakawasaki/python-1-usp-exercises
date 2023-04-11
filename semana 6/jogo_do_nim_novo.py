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
        else:
            print ('Computador começa!')
            computador_escolhe_jogada (n, m)

    else:
        print ('Você escolheu um campeonato!')

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
        else:
            print ('Computador começa!')
            computador_escolhe_jogada (n, m)



def computador_escolhe_jogada (n, m):

    nAntigo = n 
    controle = 1
    while n % (m + 1) != 0 and controle <= m:  
        n = nAntigo  
        n = n - controle 
        controle = controle + 1 

    pecasRetiradas = nAntigo - n

    print ('Tirou', pecasRetiradas, 'peça(s)')

    #return pecasRetiradas #o return só está aparecendo quando eu executo a função direto do terminal, colocando computador_escolhe_jogada (27, 3), por exemplo. é assim mesmo?

    if n != 0:
        usuario_escolhe_jogada (n, m) #usuario_escolhe_jogada (32, 3)
    else:
        print ('o computador ganhou!')


def usuario_escolhe_jogada (n, m):
    #print ('como', n, 'é múltiplo de', m, '+ 1', 'o usuário pode começar!')
    #print ('o n:', n, 'e o m:', m, 'que vieram pra cá')

    nAntigo = n
    
    pecasRetiradas = int (input ('Informe quantas peças você quer retirar: '))
    while pecasRetiradas < 1 or pecasRetiradas > m:
        print ("Você deve retirar ao menos 1 peça. E você não pode retirar mais peças do que o permitido.")
        pecasRetiradas = int (input ('Informe quantas peças você quer retirar: '))

    n = nAntigo - pecasRetiradas

    #print ('o n:', n, 'e o m:', m, 'que irão pra lá')

    if n != 0:
        computador_escolhe_jogada (n, m)
    else:
        print ('Você ganhou!')



partida ()
