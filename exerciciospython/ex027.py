nome = str(input('Qual seu nome completo ? ')).strip().upper()
print('Primeiro nome: {}'.format(nome.split()[0]))
print('Último nome: {}'.format(nome.split()[-1]))