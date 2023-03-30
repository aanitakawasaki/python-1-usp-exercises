numero = int (input ('Digite o valor de n: '))

resultado = 1 #aqui tem que ser 1 e não 0, senão o fatorial de 0 dá errado, hehe (explicação: quando o número é menor que 0, ele já pula pro print e dá print na variável resultado (que está definida com 1 e não 0), aí dá certin
resultadoAnterior = 1


while numero > 0:
    resultado = resultadoAnterior * numero
    numero = numero - 1
    resultadoAnterior = resultado

print (resultado)
