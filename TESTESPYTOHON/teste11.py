n1 = float(input('Nota de Matemática: '))
n2 = float(input('Nota de português: '))
m= (n1+n2)/2
print(" média é {:.1f}".format(m))
if m >= 6.0:
    print('ALUNO APROVADO')
else:
    print('Aluno reprovado')