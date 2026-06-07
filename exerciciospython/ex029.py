# ==============================================================================
# Exercício de Python
# Autor: Luan
# ==============================================================================
velocidade = float(input('Quantos km estava o carro? '))
if velocidade > 80:
    print('MULTADO! excedeu o limite da via de 80km/h')
    multa = (velocidade - 80) * 7
    print('Valor da multa: R${:.2f}'.format(multa))
else:
    print('No limite da via, boa viagem!')