nome = input('nome do aluno ? ')
n1 = float(input('Qual a nota de matemática ? '))
n2 = float(input('Qual a nota de português  ? '))
n3 = float(input('Qual a nota de história ? '))
n4 = n1+n2+n3
m = n4/3
print('O aluno {} tem a média de {:.2f}' .format (nome,m))