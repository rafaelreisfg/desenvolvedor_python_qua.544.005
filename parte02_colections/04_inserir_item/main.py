# bibliotecas
import os


# lista vazia
tarefas = []


# limpar terminal
os.system("cls" if os.name == "nt" else "clear")


'''
inserir = input("Deseja inserir uma tarefa? (s/n): ").lower()

while inserir == "s":
    tarefa = input("Digite a tarefa: ")
    tarefas.append(tarefa)
    inserir = input("Deseja inserir outra tarefa? (s/n): ").lower()
    if inserir == 'n':
        break

print(f'Tarefas inseridas: {tarefas}')
'''

# loop para usuário informar novas tarefas
while True:
    # menu
    print('1 - Inserir nova tarefa na lista')
    print('2 - Finalizar e exibir lista')
    opcao = input('Digite a opção [1/2]: ').strip() # informa opção desejada

    # verifica a opção informada
    match opcao:
        case '1':
            nova_tarefa = input('Informe a nova tarefa: ') # usuário informa nova tarefa
            tarefas.append(nova_tarefa) # insere item na lista
            continue # retorna para o inicio do loop
        case '2':
            os.system("cls" if os.name == "nt" else "clear")

            # exibir lista
            for n, tarefa in enumerate(tarefas, start = 1):
                print(f'{n}ª tarefa: {tarefa}')
            break # encerrar loop
        case _:
            print('Opção inválida.')
