import time
gaveta_1 = 50
gaveta_2 = 20
gaveta_3 = 10
#cliente vai digitar o valor que ele que
print('Neste caixa tem somente notas de 50, 20 e 10')
cliente = float(input('Digite o valor que deseja sacar: R$'))
if cliente % 10 != 0:
    print('Erro ! não a nota disponível.')
else:
    print('Quantas notas de 50 ? {}'.format(cliente // gaveta_1))
    cliente = cliente % gaveta_1
    print('Quantas notas de 20 ? {}'.format(cliente // gaveta_2))
    cliente = cliente % gaveta_2
    print('Quantas notas de 10 ? {}'.format(cliente // gaveta_3))
print('Processando...')
time.sleep(3)
print('Retire o dinheiro')

