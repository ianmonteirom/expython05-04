# 2. Escreva um algoritmo que solicite 10 números e exiba o dobro de cada número digitado.

cont = 1
dobro = 1

while cont <= 10:
    n = int(input('Digite um número: '))
    dobro = n * 2
    print(f'Dobro de {n}: {dobro}')
    cont += 1
    dobro = 1
