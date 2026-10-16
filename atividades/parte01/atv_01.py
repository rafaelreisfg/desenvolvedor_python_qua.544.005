'''
- Atividade 01 -

Crie um programa que receba o nome, a massa em kilogramas e a altura em metros do usuário.
Calcule o IMC.
Finalize informando o diagnóstico.
'''

nome = input('Digite o nome do paciente: ').strip().title()
massa = float(input('Digite a massa do paciente: ').replace(',','.'))
altura = float(input('Digite a altura do paciente: ').replace(',','.'))
imc = (massa / (altura ** 2))


if imc >= 40:
    print(f'{nome} está em Obesidade classe 3')
elif imc < 40 and imc >= 35:
    print(f'{nome} está em Obesidade classe 2')
elif imc < 35 and imc >= 30:
    print(f'{nome} está em Obesidade classe 1')
elif imc < 30 and imc >= 25:
    print(f'{nome} está com excesso de peso')
elif imc < 25 and imc >= 18.5:
    print(f'{nome} está no peso normal')
else:
    print(f'{nome} está abaixo do peso normal')


