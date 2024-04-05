"""
12. Faça um algoritmo que solicite um número inteiro ao usuário e calcule o fatorial desse
número. O fatorial de um número N é a multiplicação de N por seus antecessores
maiores ou iguais a 1.
Por exemplo: o fatorial de 5 é igual a 5*4*3*2*1 = 120
"""

from math import factorial

n = int(input('Digite um número inteiro para descobrir seu fatorial: '))

print(f'Fatorial de {n}: {factorial(n)}')
