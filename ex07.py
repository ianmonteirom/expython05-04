"""
7. Solicite dois números diferentes ao usuário (caso os números sejam iguais, o algoritmo
deve solicitar os números novamente) e informe a diferença entre o maior e o menor
número.
"""

n1, n2 = 0, 0
diff = 0

while n1 == n2:
    print('(Os números não podem ser iguais)')
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    diff = n1 - n2

if diff < 0:
    diff *= -1

print(f'Diferença entre os números: {diff}')
