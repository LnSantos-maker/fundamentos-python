#Desafio de Arquitetura: O Aplicativo de Mobilidade (Estilo Uber)
#Primeiro vou estabelecer as varias necessarias para o desfecho.
taxa_fixa = 4.00
taxa_km = 2.00
# agora vou acrescenta o valor se estiver chovendo.
km_dobrado = 4.00
# tambem entra o valor minimo por corrida.
minimo = 10.00
#O usuario devera  informa quantos kms vai percorrer e se está chovendo ou não.
import time
print( "=======" * 10)
cliente = float(input('Quantos kms vão ser rodados? '))
chuva = input('Está chovendo? [S/N]').strip().upper() # usei strip e lower para caso o cliente aperta espaço e para toda a resposta fica em maiusculo
print( "=======" * 10)
print('Processando...')
time.sleep(5)
print('=======' * 10)
if chuva == 'S':
    valor_total = taxa_fixa + km_dobrado * cliente
else:
   valor_total = taxa_fixa + taxa_km * cliente
# aqui  ja sabemos se o cliente pagou dobrado ou não.
if  valor_total < minimo:
    print('Total a pagar: R${:.2f}'.format(minimo))
else:
    print('Total a pagar: R${:.2f}'.format(valor_total))
print('=======' * 10)