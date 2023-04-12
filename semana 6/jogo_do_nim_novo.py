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
            n = n - (usuario_escolhe_jogada (n, m))
            print ('Você tirou', usuario_escolhe_jogada (n, m), 'peça(s)')
            print ('Agora restam', n, 'peça(s) no tabuleiro.')

            while n != 0:
                computador_escolhe_jogada (n, m)
                n = n - (computador_escolhe_jogada (n, m))
                print ('O computador tirou', computador_escolhe_jogada (n, m), 'peça(s)')
                print ('Agora restam', n, 'peça(s) no tabuleiro.')
                usuario_escolhe_jogada (n, m)
                n = n - (usuario_escolhe_jogada (n, m))
                print ('Você tirou', usuario_escolhe_jogada (n, m), 'peça(s)')
                print ('Agora restam', n, 'peça(s) no tabuleiro.')

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


"""
*Quando você muda o valor de uma variável que passou como parâmetro dentro de uma função, ao sair da função o valor não é mantido, mas o que
permanece é o valor original, então é esse o problema. 
As funções usuario_escolhe_jogada() devem somente ler a jogada do usuário, validar ela e retornar o valor e a computador_escolhe_jogada()
calcular a jogada do computador e retornar o valor também. Os prints devem ser feitos dentro da função partida, e é nela que você deve
gerenciar quantas peças estão sobrando no tabuleiro. 
Ou seja, na função partida() você chama a função para ler a jogada do usuário, e depois subtrai de n o resultado dessa função, e depois chama
a função para calcular a jogada do computador, e depois subtrai de n o resultado também. 
"""
