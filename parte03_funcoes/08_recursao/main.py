# algo que acontece dentro dele mesmo
# algo que chama a si mesmo

# bibliotecas
import os


# funções
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

# recursiva
def fatorial(n):
    return 1 if n == 1 else n * fatorial(n - 1)

# função principaç
def main():
    limpar()
    try:
        n = int(input('Digite um número inteiro: '))
        limpar()
        print(f'Fatorial de {n}! é {fatorial(n)}.')
    except Exception as e:
        print(f'Não foi possível informar o fatorial. {e}')

if __name__ == '__main__':
    main()