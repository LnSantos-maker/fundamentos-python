# ==============================================================================
# Exercício de Python
# Autor: Luan
# ==============================================================================
 #crie um programa que leia o nome completo de um pessoa e mostre:
#- o nome com todas as letras maiusculas
#- o nome com todas as letras minusculas
#quantas letras ao todo (sem considerar os espaços)
#- quantas letras tem o primeiro nome
nome = str(input('Digite seu nome completo: ')).strip()
pedaço = nome.split()
print('analisando nome...')
print('O nome em maiusculo é {}'.format(nome.upper()))
print('O nome em minusculo é {}'.format(nome.lower()))
print('o nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('O primeiro nome tem {} letras'.format(len(pedaço[0])))