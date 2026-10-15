# tratamento de exceção

try:
    nome = input('Informe seu nome: ').strip().title()
    idade = int(input('Informe sua idade: '))

    print(f'Nome do usuário: {nome}')
    print(f'Idade do usuário: {idade}')
except Exception as e:
    print(f'Não foi possível completar a ação! {e}.')
finally:
    print('Programa finalizado com sucesso!')