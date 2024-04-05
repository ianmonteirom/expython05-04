"""
11. Escreva um programa que solicita ao usuário o valor de N e calcule o valor de 𝑆 na série
abaixo:
"""

cont = 1
s = 0

n = int(input('Valor de N: '))

while cont <= n:
    s += 1/cont
    cont += 1

print(f'Valor de S: {s:.2f}')
