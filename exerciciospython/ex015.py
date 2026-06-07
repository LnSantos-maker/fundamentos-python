#escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias 
#pelos quais ele foi alugado, calucle o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.
aluguel = 60
preço_km = 0.15
dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram percorridos? '))
preço = (dias * aluguel) + (km * preço_km)
print('preço do dia: R${:.2f} \n preço do km: R${:.2f} \n dias de aluguel:{} dias \n preço a pagar R${:.2f}'.format(aluguel,preço_km,dias,preço))
