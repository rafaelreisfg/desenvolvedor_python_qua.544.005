# biliotecas
import json
import os

# lista
usuarios = []

# limpar terminal
os.system("cls" if os.name == "nt" else "clear")

#loop
while True:
    #menu
    print('1 - Cadastrar novo usuário')
    print('2 - Listar usuários cadastrados')
    print('3 - Alterar dados de um usuário')
    print('4 - Excluir dados de um usuário')
    print('5 - Gravar dados em arquivo JSON')
    print('6 - Abrir arquivo JSON e listar usuários cadastrados')
    print('7 - Sair do programa')

    opcao = input('Opção desejada: ').strip()
    os.system("cls" if os.name == "nt" else "clear")

    match opcao:
        case '1':
            # inicialiszar dicionário
            usuario = {}

            # inserção dos dados do usuário
            usuario['nome'] = input('Informe o nome do usuário: ').strip().title()
            usuario['email'] = input('Informe o e-mail do usuário: ').strip().lower()
            usuario['telefone'] = (input('Informe o telefone do usuário: ').strip())
            usuario['cpf'] = input('Informe o CPF do usuário: ').strip()

            # inserção do usuário na lista principal
            usuarios.append(usuario)
            os.system("cls" if os.name == "nt" else "clear")

            # confirmação da inserção do usuário
            print(f'{usuario.get('nome')} inserido com sucesso!') 
            continue
        case '2':
            # lista os usuários cadastrados que já foram para a lista principal
            for i, usuario in enumerate(usuarios):
                print(f'ID: {i}º')
                for chave, valor in usuario.items():
                    print(f'{chave.capitalize()}: {valor}')
                print(f'{'-'*40}')
            continue
        case '3':
            # alteração de dados do usuário
            try:
                indice = int(input('Informe o índice a ser alterado: '))
                # mostrar dicionario
                for chave, valor in usuarios[indice].items():
                    print(f'{chave.capitalize()}: {valor}.')
                chave = input('Qual chave deseja alterar o valor? ').strip().lower()
                usuarios[indice][chave] = input('Informe o novo valor: ').strip()
                os.system("cls" if os.name == "nt" else "clear")
                print(f'Dados de {usuarios[indice].get('nome')} alterado com sucesso!')

            except Exception as e:
                print(f'Não foi possível atualizar os dados. {e}')
        case '4': 
            # exclusão de dados
            try:
                indice = int(input('Informe o ID a ser excluído: '))
                del usuarios[indice]
                os.system("cls" if os.name == "nt" else "clear")
                print('Usuário excluído com sucesso.')
                continue
            except Exception as e:
                print(f'Não foi possível excluir: {e}.')
        case '5':
            # exibe os usuários cadastrados
            for usuario in usuarios:
                for chave, valor in usuario.items():
                    print(f"{chave.capitalize()}: {valor}")
                print(f"{'-'*40}")
            # pergunta ao usuário se deseja prosseguir
            gravar_dados = input("Deseja gravar os dados? (s/n)").strip().lower()
            if gravar_dados == "s":
                os.system("cls" if os.name == "nt" else "clear")
                arquivo = input("Informe o nome do arquivo: ").strip()
                with open(f"atv_01/{arquivo}.json","w",encoding="utf-8") as f:
                    json.dump(usuarios, f)
                os.system("cls" if os.name == "nt" else "clear")
                print("Arquivo json gravado com sucesso!")
                continue
            else:
                os.system("cls" if os.name == "nt" else "clear")
                continue
        case '6':
            try:
                arquivo = input('Informe o nome do arquivo que deseja abrir: ').strip()
                with open(f'atv_01/{arquivo}.json', 'r', encoding='utf-8') as f:
                    usuarios = json.load(f)
                os.system("cls" if os.name == "nt" else "clear")
                print('Dados importados com sucesso!')
                continue

            except Exception as e:
                print(f'Não foi possível abrir o arquivo. {e}.')
        case '7':
            break
        case _:
            print('Opção inválida.')

    