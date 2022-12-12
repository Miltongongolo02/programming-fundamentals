'''
Se sair de casa às 6:52 e percorrer 1 km a andar (fazendo 10 min por km), depois correr 3
km ao ritmo de 6 min por km e depois voltar a casa a andar, a que horas chego a casa
para o pequeno almoço?
2
'''

#6:52 h = 412
minutos = 412 

#percorreu 1km em 10 min 
minutos += 10

# percorreu 3 km sendo que 6 min = 1 km 
quilometro = (6 * 3) / 1

minutos += int(quilometro)

#convertendo os minutos para hora
horas = minutos // 60
minutos %= 60

print("A hora que chega em casa para o pequeno almoço é {:2d}:{:2d}".format(horas, minutos))