from math import trunc
import random
num = random.uniform(1,999)
print('O número gerado foi: {:.3f}' .format(num))
input('presione enter para mostrar a parte inteira do número: ')
print('A parte inteira do número é: {}' .format(trunc(num)))