def partida():
    print('Bem-vindo ao jogo do NIM! Escolha:')
    print('1 - para jogar uma partida isolada')
    print('2 - para jogar um campeonato')
    escolha = int(input('digite: '))
    while escolha not in [1, 2]:
        escolha = int(input('Opção inválida. Por favor, escolha 1 ou 2: '))
    if escolha == 1:
        print('Você escolheu uma partida isolada!')
        n = int(input("Quantas peças? "))
        while n < 1:
            print("Você deve colocar no mínimo 1 peça no tabuleiro!")
            n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
        while m < 1 or m > n:
            print("Você deve permitir a retirada de pelo menos 1 peça do tabuleiro. E não pode permitir a retirada de mais peças do que a quantidade total no tabuleiro")
            m = int(input("Limite de peças por jogada? "))
        jogador = 1
        while n > 0:
            print("\n")
            print("Agora restam", n, "peças no tabuleiro.")
            if jogador == 1:
                print("Sua vez!")
                pecasRetiradas = usuario_escolhe_jogada(n, m)
                jogador = 2
            else:
                print("Vez do computador!")
                pecasRetiradas = computador_escolhe_jogada(n, m)
                jogador = 1
            n = n - pecasRetiradas
        print("\n")
        print("Fim do jogo! O jogador", jogador, "ganhou!")
    else:
        print('Você escolheu um campeonato!')
        for rodada in range(1, 4):
            print('*** Rodada', rodada, ' ***')
            pontos_usuario = 0
            pontos_computador = 0
            for jogo in range(1, 4):
                print("\n")
                print("Jogo", jogo)
                n = int(input("Quantas peças? "))
                while n < 1:
                    print("Você deve colocar no mínimo 1 peça no tabuleiro!")
                    n = int(input("Quantas peças? "))
                m = int(input("Limite de peças por jogada? "))
                while m < 1 or m > n:
                    print("Você deve permitir a retirada de pelo menos 1 peça do tabuleiro. E não pode permitir a retirada de mais peças do que a quantidade total no tabuleiro")
                    m = int(input("Limite de peças por jogada? "))
                jogador = 1
                while n > 0:
                    print("\n")
                    print("Agora restam", n, "peças no tabuleiro.")
                    if jogador == 1:
                        print("Sua vez!")
                        pecasRetiradas = usuario_escolhe_jogada(n, m)
                        jogador = 2
                    else:
                        print("Vez do computador!")
                        pecasRetiradas = computador



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


#FUNCIONOU PORRA NENHUMA