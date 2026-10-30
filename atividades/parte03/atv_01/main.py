'''
# TODO: atividade 1 parte 03.

Crie um programa que calcule o peso de uma pessoa em um planeta do sistema solar.
escolhido por ela.

# NOTE: pesquisar pela gravidade de cada planeta.

# NOTE: inclua a lua na lista.
'''
import modulo as m
import os

astros = ['Mercúrio', 'Vênus', 'Terra', 'Marte', 'Júpiter', 'Saturno', 'Urano', 'Netuno', 'Lua']

m.limpar()

print(astros)

massa = int(input('Informe a sua massa: ').replace(',','.'))
planeta = input('Informe o planeta: ').strip().title()

match planeta:
    case 'Mercúrio': 
        print(m.peso(massa, 3.70))
    case 'Vênus':
        print(m.peso(massa, 8.87))
    case 'Terra':
        print(m.peso(massa, 9.80))
    case 'Marte':
        print(m.peso(massa, 3.71))
    case 'Júpiter':
        print(m.peso(massa, 24.92))
    case 'Saturno':
        print(m.peso(massa, 10.44))
    case 'Urano': 
        print(m.peso(massa, 9.01))
    case 'Netuno':
        print(m.peso(massa, 11.15))
    case 'Lua':
        print(m.peso(massa, 1.625))