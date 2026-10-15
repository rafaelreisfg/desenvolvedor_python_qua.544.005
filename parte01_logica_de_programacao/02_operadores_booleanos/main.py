'''
- usados geralmente em condicionais -

- and: duas ou mais condições verdadeiras
- or: pelo menos uma seja verdadeira
- not: obrigatóriamente falsa

'''

# declaração de variáveis

nome = input('Digite o nome: ').strip().title()
idade = int(input('Digite a idade: '))
altura = float(input('Digite a altura: ').replace(',','.')) # replace troca a vírgula pelo ponto caso o usuário digite vírgula.

# verificação de condições 

if idade >= 12 and altura >= 1.35:
    print(f'{nome} tem entrada permitida.')
else:
    print(f'{nome} tem entrada negada.')