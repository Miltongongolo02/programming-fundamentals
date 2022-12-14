import math
# You throw a dart that hits coordinates (x, y) on a dartboard.
# Create a program that gives you the score.
# See:
#   https://en.wikipedia.org/wiki/Darts#Dartboard
#   https://www.dimensions.com/element/dartboard

print("Enter the coordinates in mm from the center of the board.")
x = float(input("x? "))
y = float(input("y? "))

# Points of the sectors, clockwise from the top
# Example: the sector right from the center is POINTS[5] == 6.
POINTS = (20, 1, 18, 4, 13, 6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11, 14, 9, 12, 5)

distancia = math.sqtr(pow(x,2) + pow(y,2))
angulo = math.degrees(math.atan2(y,x))

if distancia > 170:
    print('Fora!')
    exit(1)

print(f'Ângulo: {round(angulo)}')

if angulo < 0:
    angulo += 360

if angulo < 9:
    score = POINTS[5]
elif angulo < 27:
    score = POINTS[4]
elif angulo < 45:
    score = POINTS[3]
elif angulo < 63:
    score = POINTS[2]
elif angulo < 81:
    score = POINTS[1]
elif angulo < 99:
    score = POINTS[0]
elif angulo < 117:
    score = POINTS[19]
elif angulo < 135:
    score = POINTS[18]
elif angulo < 153:
    score = POINTS[17]
elif angulo < 171:
    score = POINTS[16]
elif angulo < 181:
    score = POINTS[15]
elif angulo < 207:
    score = POINTS[14]
elif angulo < 225:
    score = POINTS[13]
elif angulo < 243:
    score = POINTS[12]  
elif angulo < 261:
    score = POINTS[11]
elif angulo < 279:
    score = POINTS[10]
elif angulo < 297:
    score = POINTS[9]
elif angulo < 315:
    score = POINTS[8]
elif angulo < 333:
    score = POINTS[7]
elif angulo < 351:
    score = POINTS[6]
else:
    score = POINTS[5]

if distancia < 12.7:
    score = 50
elif distancia < 32:
    score = 25
elif 99 < distancia < 107:
    score *= 3
elif 162 < distancia < 170:
    score *= 2

print(f'Score: {score}')