import math

#int(Input's
x1 = int(input('X1: '))
y1 = int(input('Y1: '))
x2 = int(input('X2: '))
y2 = int(input('Y2: '))

#Tratamento de dados
distancia = math.sqrt(pow((x2 - x1),2) + pow((y2 - y1),2))

#Output
print(f'A distancia entre os dois pontos é {distancia}')