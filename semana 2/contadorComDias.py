segundosDigitados = input ("Por favor, entre com o número de segundos que deseja converter: ")
segundosDigitadosNum = float (segundosDigitados)

dias = int (segundosDigitadosNum // 86400)
segundosRestDias = segundosDigitadosNum % 86400

horas = int (segundosRestDias // 3600)
segundosRestHoras = segundosRestDias % 3600

minutos = int (segundosRestHoras // 60)
segundosRestMinutos = segundosRestHoras % 60

segundos = int (segundosRestMinutos)

print (dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos.")
