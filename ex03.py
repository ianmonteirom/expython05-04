"""
3. Escreva um algoritmo que solicite a idade de 15 pessoas e informe a quantidade de
pessoas com idade inferior a 18 anos.
"""

cont = 1
menor = 0

while cont <= 15:
    idade = int(input(f'Digite a {cont}a idade: '))
    if idade < 18:
        menor += 1
    cont += 1

print(f'Pessoas menores de idade: {menor}')
