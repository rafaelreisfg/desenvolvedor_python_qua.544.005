# lista
frutas = [
    'Maçã',
    'Pêra',
    'Maracujá',
    'Morango',
    'Manga',
    'Melancia',
    'Goiaba'
]

while True:
    for n, fruta in enumerate(frutas):
        print(f'Indice {n}: {fruta}')

    # menu
    print('1 - Excluir fruta')
    print('2 - Encerrar programa')
    decisao = input('Opção desejada: ').strip()

    # verificar opção

    match decisao:
        case '1':
            indice = int(input('Qual é o índice a ser excluído?'))
            del(frutas[indice]) # exclui o índice escolhido
            print('Fruta excluída com sucesso!')
            continue
        case '2':
            break
        case _:
            print('Opção inválida.')
            continue
