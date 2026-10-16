# importa a biblioteca os
import os 

# limpa a tela
os.system('cls' if os.name == 'nt' else 'clear')

# loop
while True:
    aluno = input('Informe o nome do aluno: ').strip().title()
    
    try:
        nota_aluno = float(input('Informe uma nota de 0 a 10: ').replace(',','.'))

        if nota_aluno >= 0 and nota_aluno <= 10:
            if nota_aluno >= 7:
                print(f'{aluno} aprovado.')
            elif nota_aluno >= 5:
                print(f'{aluno} em recuperação')
            else:
                print(f'{aluno} reprovado.')
        else:
            print('Nota inválida!')

    except Exception as e:
        print(f'Não foi possível calcular a média. {e}.')

    continuar = input('Deseja inserir outra nota? "sim" para prosseguir. Qualquer outro valor para encerrar: ').strip().lower()
    
    if continuar == 'sim':
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
    else:
        print('Programa encerrado.')
        break

            