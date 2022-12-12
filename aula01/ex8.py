'''
Um livro custa 20€ a fabricar (PF). Suponha que o preço de capa de um livro é 24,95€
(PC) e que o mesmo paga uma taxa de IVA de 23% (IMP). Acresce sobre o valor do
livro uma taxa para compensar os autores pelas cópias de 0,20€ fixos (SPA).
PC = (PF + Lucro) * (100% + IMP) + SPA
Para uma tiragem de 500 exemplares: qual o lucro da livraria? Qual o total de impostos?
'''

# dados 
pc = 24.95
pf = 20
spa = 0.20
imp = 0.23

#calculo para obter o lucro por livro
lucro = (pc - spa - (pf * (1 + imp)))/(1.23)

#lucro por quantidade de livros vendidos
exemplares = int(input("Quantos livros foram vendidos? "))

lucro *= exemplares

imposto = (pc * exemplares) * imp

print("Para uma tiragem de {} Livros, a livraria teve lucro de {:.2f}€ e o total de imposto pago foi de {:.2f}€!".format(exemplares, lucro, imposto))