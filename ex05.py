"""
5. Escreva um algoritmo que solicite 15 números e informe o somatório de todos os
números ímpares digitados.
"""

cont = 1
soma_imp = 0

while cont <= 15:
    n = int(input(f'Digite o {cont}o número: '))
    if n % 2 != 0:
        soma_imp += n
    cont += 1

print(f'Soma dos números ímpares: {soma_imp}')
