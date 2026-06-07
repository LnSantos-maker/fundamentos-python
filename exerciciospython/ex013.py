salario = float(input('Digite o salário do funcionário: R$'))
aumento = 0.15
novo_salario = salario + (salario * aumento)
print('antigo salário: R${:.2f} \n Novo salário com aumento de 15%: R${:.2f}' .format(salario,novo_salario))
desconto = 0.09
salario_com_desconto = novo_salario - (novo_salario * desconto)
print('Salario com desconto do inss: R${:.2f}' .format(salario_com_desconto))