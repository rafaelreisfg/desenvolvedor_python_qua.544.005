import os
from modulo import limpar, peso_astro

def main():
    astros = {        
        'Mercúrio': 3.73,
        'Vênus': 8.73,
        'Terra': 9.8,
        'Lua': 1.62,
        'Marte': 3.73,
        'Júpiter': 24.92,
        'Saturno': 10.5,
        'Urano': 8.73,
        'Netuno': 11.77, 
    }

    limpar()
    massa = float(input('Informe sua massa em kg: ').replace(',','.'))

    for chave, valor in astros.items():
        print(f'{chave.upper()}:')
        print(f'Gravidade: {valor} m/s²')
        print(f'Peso: {peso_astro(massa, valor):.2f} N')    
        print(f'{'-'*40}')

if __name__ == '__main__':
    main()
