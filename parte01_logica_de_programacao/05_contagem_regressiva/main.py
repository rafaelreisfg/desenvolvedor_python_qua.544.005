import os
import time

# limpar terminal

os.system('cls')

# entrada de dados

numero = int(input('Informe um número inteiro: '))

# loop

while numero >= 0:
    os.system('cls')
    print(f'{numero}...')
    time.sleep(1)
    numero -= 1

print('BOOOM!!!')