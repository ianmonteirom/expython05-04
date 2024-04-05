"""
6. Solicite vários números ao usuário (até que ele digite o número zero) e informe o
somatório dos números digitados.
"""

cont = 1
soma = 0

while True:
    n = int(input(f'Digite o {cont}o número: [0 para] '))
    if n == 0:
        break
    soma += n
    cont += 1

print(f'Soma de todos os números digitados: {soma}')
