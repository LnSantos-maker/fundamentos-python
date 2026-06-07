peso = float(input('Qual o seu peso ? (kg) '))
altura = float(input('Qual a sua altura ? (m) '))
imc = peso/altura**2
print('O seu peso é {} kg, a sua altura é {:.2f} m e o seu IMC é {:.2f}' .format (peso,altura,imc))