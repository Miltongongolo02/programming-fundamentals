import math

#input's 
catetoA = float(input('cateto A: '))
catetoB = float(input('cateto B: '))

#Tratamento de dados
hypot = math.hypot(catetoA, catetoB)
angulo = math.degrees(math.sin(catetoA / hypot))

#Output's
print('A hipotenusa do triângulo é {:.2f}! \nO Angulo formado pelo cateto A e a hipotenusa é {:.2f}!'.format(hypot,angulo))