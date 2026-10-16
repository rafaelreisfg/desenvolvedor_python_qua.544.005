'''
Crie um programa em que o usuário informe uma única vez o nome e a idade, e em seguida,
o programa exibe uma lista de filmes do cinema e suas respectivas salas e classificações indicativas.

O usuário deverá escolher a sala do filme desejado. Se tiver idade mínima, o programa imprime o ingresso e encerra.
Senão, o programa impede a entrada do usuário e retorna a lista para que o mesmo possa escolher outro filme
'''

nome = input('Digite o seu nome: ').strip().title()
idade = int(input('Digite a sua idade: ').replace(',','.'))

print('Filme 1 - Sala 1 - Classificação Livre')
print('Filme 2 - Sala 2 - Classificação 10 anos')
print('Filme 3 - Sala 3 - Classificação 14 anos')
print('Filme 4 - Sala 4 - Classificação 16 anos')
print('Filme 5 - Sala 5 - Classificação 18 anos')

escolha = input('Digite o filme que deseja: ')

while True:

    match escolha:
        case '1':
            print('Filme 1 - Sala 1 - Classificação Livre')
        case '2':
            if idade < 10:
                print(f'{nome} não tem idade para ver esse filme')
                break
            else:
                print('Imprimindo ingresso...')             
        case '3':
            if idade < 14:
                print(f'{nome} não tem idade para ver esse filme')
                break
            else:
                print('Imprimindo ingresso...')
        case '4':
            if idade < 16:
                print(f'{nome} não tem idade para ver esse filme')
                break
            else:
                print('Imprimindo ingresso...')
        case '5':
            if idade < 18:
                print(f'{nome} não tem idade para ver esse filme')
                break
            else:
                print('Imprimindo ingresso...')
                break
