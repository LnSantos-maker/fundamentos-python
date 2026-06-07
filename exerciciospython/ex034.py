salario = float(input('Qual o salário do funcionário? R$'))      
if salario  >= 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15
aumento_salario =  aumento + salario  
print('O novo salário é de R${:.2f}'.format(aumento_salario))   
    