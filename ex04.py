"""
4. Escreva um algoritmo que solicite 10 números e informe quantos números entre 100 e
200 foram digitados.
"""

cont = 1
entre = 0

while cont <= 10:
    n = int(input(f'Digite o {cont}o número: '))
    if 100 <= n <= 200:
        entre += 1
    cont += 1

print(f'Números digitados entre 100 e 200: {entre}')
