#dados do problema
andares = int(input("Andares? "))  # numero além do R/C
moradores = int(input("Moradores por andar? "))
altura = 3      # altura de um andar (m)
velocidade = 1  # m/s 

# tratamento de dados 
distancia = 365 * altura *4 * moradores * (andares + 1) * andares / 2
segundos = int(distancia / velocidade) 
h = segundos // 3600
m = (segundos % 3600) // 60
s = (segundos % 3600) % 60

print("Durante um ano o elevador percorre {} Km".format(distancia/1000))

print("durante um ano o elevador funciona por {:02d}:{:02d}:{:02d} horas".format(h, m, s))