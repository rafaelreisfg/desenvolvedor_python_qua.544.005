# superclasse / classe pai

class Pessoa:
    def __init__(self, email, telefone, endereco):
        self.email = email
        self.telefone = telefone
        self.endereco = endereco

# subclasses / classes filhas

class PessoaFisica(Pessoa):
    def __init__(self, nome, cpf, email, telefone, endereco):
        self.nome = nome
        self.cpf = cpf
        super.__init__(email=email, telefone=telefone, endereco=endereco)

class PessoaJuridica(Pessoa):
    def __init__(self, cnpj, razao_social, nome_fantasia, email, telefone, endereco):
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        super.__init__(email=email, telefone=telefone, endereco=endereco)