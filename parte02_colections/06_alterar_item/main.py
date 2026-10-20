# biblioteca
import os


# lista
nomes = [
    'Alex',
    'Charlote',
    'Scarlet',
    'John',
    'Jason',
    'Michael',
    'Connor'
]

os.system('cls' if os.name == 'nt' else 'clear')


while True:
    # exibe a lista original
    for n, nome in enumerate(nomes):
        print(f'Indice {n}: {nome}')


    # menu
    print('1 - Alterar item da lista')
    print('2 - Finalizar')
    decisao = input('Opção escolhida: ').strip()


    # verifica a opção escolhida
    match decisao:
        case '1':
            # informa índice a ser alterado
            indice = int(input('Informe o índice a ser alterado: '))
            # informa novo valor 
            nomes[indice] = input('Informe novo nome: ').strip().title()
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Item da lista alterado com sucesso.')
            continue
        case '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            # exibir nova lista
            for n, nome in enumerate(nomes):
                print(f'Indice {n}: {nome}')
            break
        case _:
            print('Opção inválida')
            continue

