#Crie um programa que leia o nome de uma pessoa e diga se ela tem silva ou não
nome= str(input('Qual seu nome completo ? ')).strip().upper()
print('SILVA' in nome)