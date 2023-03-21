x1 = float (input ('digite a coordenada X de um ponto: '))
y1 = float (input ('digite a coordenada Y desse ponto: '))
x2 = float (input ('digite a coordenada X de um segundo ponto: '))
y2 = float (input ('digite a coordenada Y desse segundo ponto: '))

import math

distancia = math.sqrt ((x1 - x2)**2 + (y1 - y2)**2)

if distancia >= 10:
    print ('longe')
else:
    print ('perto')
