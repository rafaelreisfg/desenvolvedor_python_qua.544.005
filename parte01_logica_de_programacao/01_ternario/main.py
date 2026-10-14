#Declaração de variáveis

nome = input('Digite o nome: ').strip().title() # strip() -> cancela espaços. title() -> deixa as primeiras letras maísculas.
idade = int(input('Digite a idade: '))

print(f'{nome} {'é maior de idade' if idade >= 18 else 'é menor de idade.'}')