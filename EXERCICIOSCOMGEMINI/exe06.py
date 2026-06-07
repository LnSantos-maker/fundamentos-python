# ==============================================================================
# Exercício de Python
# Autor: Luan
# ==============================================================================
largura = float(input('Qual a largura da parede ? (m) '))
altura = float(input('Qual a altura da parede ? (m) '))
area = largura*altura
tinta = area/2
print ('A largura da parede é {} m, a altura da parede é {} m, a área da parede é {} m² e a quantidade de tinta necessária para pintar a parede é {} litros' .format(largura,altura,area,tinta))