#Jogo da adivinhação

import random
import time

pc = random.randint(0, 10)
print('Sou o computador\nEstou pensando em um número de 0 a 10\n')

jogando = True

while jogando:
    numero = int(input("Digite aqui seu palpite do que estou pensando: "))

    if numero == pc:
        print(f'Parabéns, você acertou, pensei no número {pc}')
        break
    if numero < pc:
        print('Mais...Tente novamente')
    elif numero > pc:
        print('Menos...Tente novamente')
