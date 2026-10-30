class Pessoa:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}. Tenho {self.idade} anos e meu e-mail é {self.email}.'