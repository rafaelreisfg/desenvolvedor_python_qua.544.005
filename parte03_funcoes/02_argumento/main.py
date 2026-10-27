import os
# função
def boas_vindas(nome):
    print(f'Seja bem-vindo, {nome}!')

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')


# algoritmo
limpar()
nome = input('Informe seu nome: ').strip().title()
boas_vindas(nome)