km = int(input("Quantos km's foram percorridos ? "))
print('Foram percorridos {}km'.format(km))
carro = float(input('qual o consumo do carro por km ?'))
print('O consumo é de {} litros por km'.format(carro))
consumo = km/ carro
print('O consumo total do carro é de {} litros'.format(consumo))
preço = 5.50
gasto = consumo * preço
print('O gasto total com combustivel é de R${:.2f}'.format(gasto))
