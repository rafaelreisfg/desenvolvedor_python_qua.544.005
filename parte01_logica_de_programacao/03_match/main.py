# declaração

valor_1 = float(input('Digite o primeiro valor: ').replace(',','.'))
valor_2 = float(input('Digite o segundo valor: ').replace(',','.'))

# menu

print(f'{'-' * 20} Escolha uma operação: {'-' * 20}')

print('1 - soma')
print('2 - subtração')
print('3 - Multiplicação')
print('4 - Divisão')

operador = input('Operação desejada: ').strip()

# match case

match operador:
    case '1':
        print(f'Resultado da soma: {valor_1 + valor_2}')
    case '2':
        print(f'Resultado da subtração: {valor_1 - valor_2}')
    case '3':
        print(f'Resultado da multiplicação: {valor_1 * valor_2}')
    case '4':
        print(f'Resultado da divisão: {valor_1 / valor_2}')
    case _:
        print('Operação inválida')