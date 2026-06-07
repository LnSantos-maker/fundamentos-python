n1 = float(input('Qual o valor do produto ? R$'))
d = n1*0.05
print('O valor do produto é R${:.2f}, com 5% de desconto fica R${:.2f}' .format(n1, n1-d))