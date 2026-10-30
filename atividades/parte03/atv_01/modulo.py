'''
# TODO: atividade 1 parte 03

Crie um programa que calcule o peso de uma pessoa em um planeta do sistema solar
escolhido por ela.

# NOTE: pesquisar pela gravidade de cada planeta
'''
import os

def limpar():
    return os.system('cls' if os.name == 'nt' else 'clear')

def peso(massa, aceleracao_gravidade):
    return (f'Seu peso é {massa * aceleracao_gravidade}')

def peso_astro(massa, gravidade
               ):
    return massa * gravidade

