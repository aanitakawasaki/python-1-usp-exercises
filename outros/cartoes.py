meuCartao = int (input ('digite o número do seu cartão de crédito: '))
outrosCartoes = 1
acheiMeuCartao = False

while outrosCartoes != 0 and not acheiMeuCartao:
    outrosCartoes = int (input ('digite o número de outros cartões de crédito: '))
    if outrosCartoes == meuCartao:
        acheiMeuCartao = True

if acheiMeuCartao:
    print ('EBA! achei meu cartão')
else:
    print ('xiii, não achei meu cartão')
