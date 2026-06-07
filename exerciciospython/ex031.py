# ==============================================================================
# Exercício de Python
# Autor: Luan
# ==============================================================================
viagem = float(input('Qual a Distancia da viagem? '))
if viagem <= 200:
    total_a_pagar = viagem * 0.50
else:
    total_a_pagar = viagem * 0.45
print('Total da viagem é de R${:.2f}'.format(total_a_pagar))    