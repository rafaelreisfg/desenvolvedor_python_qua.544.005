# biblioteca
import os


# lista de usuários
usuarios = []


# limpar terminal
os.system('cls' if os.name == 'nt' else 'clear')


# loop
while True:
    # menu
    print('1 - Cadastrar novo usuário')
    print('2 - Exibir lista de usuários')
    print('3 - sair do programa')
    opcao = input('Opção desejada: ').strip()

    os.system('cls' if os.name == 'nt' else 'clear')

    # verificar escolha
    match opcao:
        case '1': 
            # criar novo dicionário
            usuario = {}

            # insere dados no dicionário
            usuario['nome'] = input('Informe o nome do novo usuário: ').strip().title()
            usuario['idade'] = int(input('Informe a idade do novo usuário: '))
            usuario['email'] = input('Informe o e-mail do novo usuário: ').strip().title()
            usuario['cpf'] = input('Informe o cpf do novo usuário: ').strip()

            # adiciona o novo usuário a lista
            usuarios.append(usuario)

            # mensagem de sucesso
            print(f'{usuario.get('nome')} cadastrado com sucesso!')
        case '2':
            # exibe a lista de usuáruios
            for usuario in usuarios:
                for chave, valor in usuario.items():
                    print(f'{chave.capitalize()}: {valor}')
                print(f'{'-'*40}')
        case '3':
            break
        case _:
            print('Opção inválida.')
            continue