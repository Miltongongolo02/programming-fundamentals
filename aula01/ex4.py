#input
segundos = int(input('Introduza os segundos que pretende converter: '))

#Tratamento de dados
hh = segundos // 3600
mm = (segundos % 3600) // 60
ss = (segundos % 3600) % 60

#Output
print('{:02d}:{:02d}:{:02d}'.format(hh,mm,ss))