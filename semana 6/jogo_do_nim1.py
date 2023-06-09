"""
>OK n: número de peças inicial
>OK m: número máximo de peças que se pode tirar por rodada (o mínimo é 1)
> quem tirar as últimas peças possíveis ganha o jogo
> estratégia para ganhar: deixar sempre múltiplos de (m+1) peças ao jogador oponente, caso não role, tirar o máximo
de peças possíveis (?)
>OK se n já for múltiplo de (m+1), o jogador começa (computador diz "Você começa!")
>OK senão o computador começa ("Computador começa!")
> funções a serem implementadas:
.computador_escolhe_jogada: recebe, como parâmetros, os números n e m descritos acima e devolve um inteiro
correspondente à próxima jogada do computador (ou seja, quantas peças o computador deve retirar do tabuleiro) de
acordo com a estratégia vencedora.
.usuario_escolhe_jogada: recebe os mesmos parâmetros, solicita que o jogador informe sua jogada e verifica se o
valor informado é válido. se o valor informado for válido, a função deve devolvê-lo; caso contrário, deve solicitar
novamente ao usuário que informe uma jogada válida.
.partida: não recebe nenhum parâmetro, solicita ao usuário que informe os valores de n e m e inicia o jogo,
alternando entre jogadas do computador e do usuário (ou seja, chamadas às duas funções anteriores). a escolha da
jogada inicial deve ser feita em função da estratégia vencedora, como dito anteriormente. a cada jogada, deve ser
impresso na tela o estado atual do jogo, ou seja, quantas peças foram removidas na última jogada e quantas restam
na mesa. quando a última peça é removida, essa função imprime na tela a mensagem "O computador ganhou!" ou "Você
ganhou!" conforme o caso.
> observe que, para isso funcionar, seu programa deve sempre "lembrar" qual é o número de peças atualmente no
tabuleiro e qual é o máximo de peças a retirar em cada jogada
> o corretor automático não funciona bem se você tiver alguma chamada a input() antes da definição de todas as
funções do jogo (a menos que essa chamada esteja dentro de uma função). se seu programa usar input() sem que ele
esteja dentro de alguma função, coloque-o no final do programa
"""


 
def computador_escolhe_jogada (n, m):
    pecas_tiradas = m #5
    sobra = 0 #0  
    nao_sobra_multiplo = True #True 
    sobra_multiplo = True #True
    
    while pecas_tiradas > 1 and nao_sobra_multiplo: #True and True #True and True #True and True #True and True #False and True
        sobra = n - pecas_tiradas #25 #26 #27 #28
        sobra_multiplo = sobra % (m + 1) == 0 #25 % 6 != 0 False #False #False #False
        nao_sobra_multiplo != sobra_multiplo #se sobra_multiplo é False, nao_sobra_multiplo é True #True #True #True

        if nao_sobra_multiplo: #True #True #True #True
            pecas_tiradas = pecas_tiradas - 1 #4 #3 #2 #1 

    return pecas_tiradas

#vamos testar com esses valores: computador_escolhe_jogada (30, 5)
    
def partida ():
    n = int (input ('Quantas peças? '))

    while n <= 0:
        print ('Inválido. O número de peças inicial deve ser no mínimo 1')
        n = int (input ('Quantas peças? '))
        
    m = int (input ('Limite de peças por jogada? '))

    while m <= 0 or m >= n:
        print ('Inválido. O limite de peças por jogada deve ser no mínimo 1 e menor que o número de peças inicial')
        m = int (input ('Limite de peças por jogada? '))
    
    if n % (m+1) == 0:
        print ('Você começa!')
    else:
        print ('Computador começa!')
        #computador_escolhe_jogada (n, m) #aqui essa função não é chamada, pois não tem os valores de n e m (que estão fora dessa condição (?))
        
    computador_escolhe_jogada (n, m) #aqui essa função até é chamada, pois recebe os valores de n e m, mas o problema é que não dá para eu atrelá-la a uma condição, ela vai ser chamada indepentende das condições acima serem verdadeiras ou falsas. o que fazer?


 
print ('Bem-vindo ao jogo do NIM! Escolha:')
print ('1 - para jogar uma partida isolada')
print ('2 - para jogar um campeonato')
escolha_digitada = (input ('digite 1 ou 2: '))

if escolha_digitada == '1':
    print ('Você escolheu uma partida isolada!')
    partida ()
if escolha_digitada == '2':
    print ('Você escolheu um campeonato!')
