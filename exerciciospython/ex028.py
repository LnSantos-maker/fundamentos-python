import random
usuario = int(input('Em que número o Computador pensou de 0 a 5? '))
num = random.randint(0, 5)
if usuario == num:
    print('Parabéns, você acertou!')
else:
    print('Você errou!')
print('O número pensado foi: {}'.format(num))    
