"""
9. Faça um algoritmo que solicite N números e calcule a média dos números pares e a
média dos números ímpares (o valor de N deve ser solicitado ao usuário no início do
programa).
"""

qnt = int(input('Quantos números deseja calcular? '))
cont = 1
soma_par, soma_impar, qnt_par, qnt_impar = 0, 0, 0, 0

while cont <= qnt:
    n = int(input(f'Digite o {cont}o número: '))
    if n % 2 == 0:
        soma_par += n
        qnt_par += 1
    elif n % 2 != 0:
        soma_impar += n
        qnt_impar += 1
    cont += 1

media_par = soma_par / qnt_par
media_impar = soma_impar / qnt_impar

print(f'Média dos números pares: {media_par:.2f}\n'
      f'Média dos números ímpares: {media_impar:.2f}')
