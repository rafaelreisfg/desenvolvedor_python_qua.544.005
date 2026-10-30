# classe
# atributos: valores. Nome, idade, telefone
# métodos: ações
import os
os.system('cls' if os.name == 'nt' else 'clear')

class Pessoa:
    # construtor
    def __init__(self, nome, idade, email, cpf):
        # atributos
        self.nome = nome
        self.idade = idade
        self.email = email
        self.cpf = cpf
    
    def exibir_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade} anos.')
        print(f'E-mail: {self.email}')
        print(f'CPF: {self.cpf}')

def main():
    # instânciar a classe
    usuario = Pessoa(nome='', idade=0, email='', cpf='')

    # insere valores nos atributos
    usuario.nome = input('Informe seu nome: ').strip().title()
    usuario.idade = int(input('Informe sua idade: '))
    usuario.email = input('Informe seu e-mail: ').strip().lower()
    usuario.cpf = input('Informe seu CPF: ').strip()

    # exibe os atributos na tela
    os.system('cls' if os.name == 'nt' else 'clear')
    usuario.exibir_dados()

if __name__ == '__main__':
    main()