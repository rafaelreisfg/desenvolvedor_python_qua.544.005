import os
from model import PessoaFisica, PessoaJuridica

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    # instanciar as classes
    usuario = PessoaFisica(nome='', cpf='', email='', telefone='', endereco='')
    empresa = PessoaJuridica(cnpj='', razao_social='', nome_fantasia='',email='', telefone='', endereco='')

    # informar os dados do usuário
    limpar()
    print(f'{'-' * 20} Informe os dados do usuário {'-'*20}\n')
    usuario.nome = input('Informe o nome: ').strip().title()
    usuario.cpf = input('Informe o cpf: ').strip()
    usuario.email = input('Informe o e-mail: ').strip().lower()
    usuario.telefone = input('Informe o telefone: ').strip()
    usuario.endereco = input('Informe o endereço: ').strip()

    # informar os dados da empresa
    limpar()
    print(f'{'-' * 20} Informe os dados da empresa {'-'*20}\n')
    empresa.razao_social = input('Informe a razão social: ').strip()
    empresa.nome_fantasia = input('Informe o nome: ').strip().title()
    empresa.cnpj = input('Informe o cnpj: ').strip()
    empresa.email = input('Informe o e-mail: ').strip().lower()
    empresa.telefone = input('Informe o telefone: ').strip()
    empresa.endereco = input('Informe o endereço: ').strip()

if __name__ == '__main__':
    main()