# ==============================================================================
# Exercício de Python
# Autor: Luan
# ==============================================================================
reta1= float(input('Qual o valor da primeira reta? '))
reta2 = float(input('Qual valor da segunda reta? '))
reta3 = float(input('Qual valor da terceira reta? '))
# O "and" obriga que as 3 regras sejam verdadeiras ao mesmo tempo
#if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
#   print('Forma triângulo')
#else:
   # print('Não forma triângulo')
if reta1 < reta2 + reta3:
    if reta2 < reta1 + reta3:
        if reta3 < reta1 + reta2:
            print('É um triangulo')
        else:
            print('Não é um triangulo')
    else:
        print('Não é um triangulo')
else:
    print('Não é um triangulo')