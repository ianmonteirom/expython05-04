"""
10. Chico tem 1,50m e cresce 2 centímetros por ano, enquanto Juca tem 1,10m e cresce 5
centímetros por ano. Considerando que Chico e Juca continuem crescendo
constantemente, escreva um algoritmo que calcule quantos anos seriam necessários
para Juca ser mais alto que Chico.
"""

chico = 150
juca = 110
anos = 0

while juca < chico:
    chico += 2
    juca += 5
    anos += 1

print(f'Anos necessários para Juca ultrapassar Chico: {anos}')
