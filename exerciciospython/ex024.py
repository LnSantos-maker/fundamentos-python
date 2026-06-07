# ==============================================================================
# Exercício de Python
# Autor: Luan
# ==============================================================================
#crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
cidade = str(input('Nome da cidade: ')).strip().upper()
print(cidade[:5] == 'SANTO')
