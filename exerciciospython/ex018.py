# ==============================================================================
# Exercício de Python
# Autor: Luan
# ==============================================================================
import math
num = float(input('Qual o valor do ângulo:'))
angulo = math.radians(num)
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)
print('O valor do seno é: {:.2f} \n O valor do cosseno é: {:.2f} \n O valor da tangente é: {:.2f}' .format(seno, cosseno, tangente))