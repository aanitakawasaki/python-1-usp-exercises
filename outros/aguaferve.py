#temperaturaAgua = input ('coloque a temperatura da água: ')
#temperaturaAguaNum = float (temperaturaAgua)
#ou simplesmente:
temperaturaAgua = float (input ('coloque a temperatura da água: '))
if temperaturaAgua > 100:
    aguaFerve = True
    print ('água ferveu')
#aguaFerve = False
#print ('água não ferveu')
#isso aqui dá errado, porque não funciona como um else do if, funciona como a continuação do código (que vai ser executada seja a condição do if false ou true)
#o ideal seria fazer isso aqui:
if temperaturaAgua <= 100:
    aguaFerve = False
    print ('água não ferveu')
#ooou, usar a estrutura else mesmo, vou usar no "aguaferveB.py"
