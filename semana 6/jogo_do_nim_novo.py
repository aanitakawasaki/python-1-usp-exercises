"""
> funções a serem implementadas:
.OKcomputador_escolhe_jogada: recebe, como parâmetros, os números n e m descritos acima e devolve um inteiro
correspondente à próxima jogada do computador (ou seja, quantas peças o computador deve retirar do tabuleiro) de
acordo com a estratégia vencedora.
.OKusuario_escolhe_jogada: recebe os mesmos parâmetros, solicita que o jogador informe sua jogada e verifica se o
valor informado é válido. se o valor informado for válido, a função deve devolvê-lo; caso contrário, deve solicitar
novamente ao usuário que informe uma jogada válida.
.partida: não recebe nenhum parâmetro, solicita ao usuário que informe os valores de n e m e inicia o jogo,
alternando entre jogadas do computador e do usuário (ou seja, chamadas às duas funções anteriores). a escolha da
jogada inicial deve ser feita em função da estratégia vencedora, como dito anteriormente. a cada jogada, deve ser
impresso na tela o estado atual do jogo, ou seja, quantas peças foram removidas na última jogada e quantas restam
na mesa. quando a última peça é removida, essa função imprime na tela a mensagem "O computador ganhou!" ou "Você
ganhou!" conforme o caso.
>OK observe que, para isso funcionar, seu programa deve sempre "lembrar" qual é o número de peças atualmente no
tabuleiro e qual é o máximo de peças a retirar em cada jogada
>OK o corretor automático não funciona bem se você tiver alguma chamada a input() antes da definição de todas as
funções do jogo (a menos que essa chamada esteja dentro de uma função). se seu programa usar input() sem que ele
esteja dentro de alguma função, coloque-o no final do programa
"""



"""
EXEMPLO 1 [n é múltiplo de (m+1), portanto o usuário começa "Você começa!"]:

Defina o número de peças (n): 20
Defina o número máximo de peças que podem ser retiradas por jogada (m): 3

[Estratégia vencedora: deixar sempre múltiplos de (m+1), no caso: múltiplos de 4, peças ao jogador oponente, caso
 não role, tirar o máximo de peças possíveis!]

USUÁRIO começa!
[como o número de peças no tabuleiro (20) já é úm múltiplo de 4, o computador já conseguiu esse feito (de deixar
no tabuleiro sempre um múltiplo de (m+1), então o usuário pode começar!]

Quantidade de peças no tabuleiro: 20
Quantidade de peças removidas pelo USUÁRIO: 3 [se ele retirasse 3 peças, sobrariam 17 (não é múltiplo de 4), se ele
retirasse 2 também não (sobraria 18 - não é múltiplo de 4), se ele retirasse 1 (sobraria 19 - não é múltiplo de 4).
mas como ele tem que tirar o máximo de peças possível, caso não consiga transformar o número de peças restantes em
um múltiplo de 4, ele tira 3 mesmo]

Número de peças restantes: 17
Quantidade de peças removidas pelo COMPUTADOR: 1 [se ele tirar 3, sobram 14 (não múltiplo de 4), se ele tirar 2,
sobram 15 (não múltiplo de 4), se ele tirar 1, sobram 16 (múltiplo de 4!). portanto, ele tira 1 peça! e está
implementando bem a estratégia vencedora!]

Número de peças restantes: 16
Quantidade de peças removidas pelo USUÁRIO: 3 [máximo]

Número de peças restantes: 13
Quantidade de peças removidas pelo COMPUTADOR: 1 [sobra múltiplo de 4]

Número de peças restantes: 12
Quantidade de peças removidas pelo USUÁRIO: 3 [máximo]

Número de peças restantes: 9
Quantidade de peças removidas pelo COMPUTADOR: 1 [sobra múltiplo de 4]

Número de peças restantes: 8
Quantidade de peças removidas pelo USUÁRIO: 3 [máximo]

Número de peças restantes: 5
Quantidade de peças removidas pelo COMPUTADOR: 1 [sobra múltiplo de 4]

Número de peças restantes: 4
Quantidade de peças removidas pelo USUÁRIO: 3 [máximo]

Número de peças restantes: 1
Quantidade de peças removidas pelo COMPUTADOR: 1

O computador escolhe remover a 1 peça restante e ganha o jogo.

Nesse exemplo, o computador venceu a partida. Ele seguiu a estratégia de deixar sempre um número múltiplo de 4
(m+1) de peças para o jogador, e quando isso não era possível, retirou o máximo de peças permitidas. O usuário, por
sua vez, não conseguiu evitar que o computador seguisse sua estratégia vencedora e acabou perdendo a partida.



EXEMPLO 2 [n não é múltiplo de (m+1), então o computador começa "Computador começa!"]:

Defina o número de peças (n): 21
Defina o número máximo de peças que podem ser retiradas por jogada (m): 3

[Estratégia vencedora: deixar sempre múltiplos de (m+1), no caso: múltiplos de 4, peças ao jogador oponente, caso
 não role, tirar o máximo de peças possíveis!]

COMPUTADOR começa!
[como o número de peças no tabuleiro (21) não é úm múltiplo de 4, o computador começa para tentar conseguir mudar
isso]

Quantidade de peças no tabuleiro: 21
Quantidade de peças removidas pelo COMPUTADOR: 1 [se ele retirasse 3 peças, sobrariam 18 (não é múltiplo de 4), se
ele retirasse 2 também não (sobraria 19 - não é múltiplo de 4), já se ele retirasse 1, sobraria 20 (que é um
múltiplo de 4 - estratégia implementada!).

Quantidade de peças no tabuleiro: 20
Quantidade de peças removidas pelo USUÁRIO: 3 [se ele retirasse 3 peças, sobrariam 17 (não é múltiplo de 4), se ele
retirasse 2 também não (sobraria 18 - não é múltiplo de 4), se ele retirasse 1 (sobraria 19 - não é múltiplo de 4).
mas como ele tem que tirar o máximo de peças possível, caso não consiga transformar o número de peças restantes em
um múltiplo de 4, ele tira 3 mesmo]

Número de peças restantes: 17
Quantidade de peças removidas pelo COMPUTADOR: 1 [se ele tirar 3, sobram 14 (não múltiplo de 4), se ele tirar 2,
sobram 15 (não múltiplo de 4), se ele tirar 1, sobram 16 (múltiplo de 4!). portanto, ele tira 1 peça! e está
implementando bem a estratégia vencedora!]

Número de peças restantes: 16
Quantidade de peças removidas pelo USUÁRIO: 3 [máximo]

Número de peças restantes: 13
Quantidade de peças removidas pelo COMPUTADOR: 1 [sobra múltiplo de 4]

Número de peças restantes: 12
Quantidade de peças removidas pelo USUÁRIO: 3 [máximo]

Número de peças restantes: 9
Quantidade de peças removidas pelo COMPUTADOR: 1 [sobra múltiplo de 4]

Número de peças restantes: 8
Quantidade de peças removidas pelo USUÁRIO: 3 [máximo]

Número de peças restantes: 5
Quantidade de peças removidas pelo COMPUTADOR: 1 [sobra múltiplo de 4]

Número de peças restantes: 4
Quantidade de peças removidas pelo USUÁRIO: 3 [máximo]

Número de peças restantes: 1
Quantidade de peças removidas pelo COMPUTADOR: 1

O computador escolhe remover a 1 peça restante e ganha o jogo.

Nesse exemplo, o computador venceu a partida. Ele seguiu a estratégia de deixar sempre um número múltiplo de 4
(m+1) de peças para o jogador, e quando isso não era possível, retirou o máximo de peças permitidas. O usuário, por
sua vez, não conseguiu evitar que o computador seguisse sua estratégia vencedora e acabou perdendo a partida.

"""



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

    return pecasRetiradas #o return só está aparecendo quando eu executo a função direto do terminal, colocando computador_escolhe_jogada (27, 3), por exemplo. é assim mesmo?



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
