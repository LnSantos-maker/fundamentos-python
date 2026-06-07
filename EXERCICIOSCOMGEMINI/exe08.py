placa_de_video = float(input('Qual o valor da placa de video ? R$'))
teclado = float(input('Valor do teclado ? R$'))
mouse = float(input('Valor do mouse ? R$'))
desconto = placa_de_video * 0.15
deconto_teclado = teclado * 0.15
desconto_mouse = mouse * 0.15
preco_final  = placa_de_video - desconto + teclado - deconto_teclado + mouse - desconto_mouse
print('O valor de cada item com desconto será: \n placa de video R${:.2f} \n teclado R${:.2f} \n mouse R${:.2f} \n O VALOR TOTAL DOS SEUS INTENS COM DESCONTO É DE R${:.2f}' .format(placa_de_video - desconto, teclado - deconto_teclado, mouse - desconto_mouse, preco_final))