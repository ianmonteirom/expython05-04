"""
8. Escreva um algoritmo que solicite 10 números e informe qual foi o menor número
digitado.
"""

menor = 99999999999999999999
cont = 1

while cont <= 10:
    n = int(input(f'Digite o {cont}o número: '))
    if n < menor:
        menor = n
    cont += 1

print(f'Menor número entre os 10 valores: {menor}')
