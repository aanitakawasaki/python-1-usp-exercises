numeroInteiro = input ("Digite um número inteiro: ")
numeroInteiroNum = int (numeroInteiro)


resultadoInteiro = numeroInteiroNum // 10

resultadoResto = resultadoInteiro % 10

dezena = int (resultadoResto)

print ("O dígito das dezenas é", dezena)
