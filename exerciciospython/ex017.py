# ==============================================================================
# Exercício de Python
# Autor: Luan
# ==============================================================================
import math
num1 = float(input('Qual o valor do cateto oposto? '))
num2 = float(input('Qual o valor do cateto adjacente? '))
hipotenusa = math.hypot(num1,num2)
print('O valor da hipotenusa é: {:.2f}' .format(hipotenusa))