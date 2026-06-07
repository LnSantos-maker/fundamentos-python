print('---------------------------------------------------------------')
num1 = int(input('Qual o primeiro número? ').strip())
num2 = int(input('Qual o segundo número? ').strip())
num3 = int(input('Qual o terceiro número? ').strip())
print('--------------------------------------------------------------')
print(f'Dados os números {num1},{num2},{num3} ')
menor = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3
maior = num1
if num2 >  maior:
    maior = num2
if num3 > maior:
    maior = num3
print(f'O número menor foi {menor}.')
print(f'O número maior foi {maior}.')