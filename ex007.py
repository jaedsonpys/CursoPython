# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aléatorios.
# Guarde em um dicionário. No final, coloque esse dicionario em ordem, sabendo que
# o vencedor tirou o maior número de dado

from random import randint

jogadores = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}

for k, v in jogadores.items():
    print(f'O {k} tirou o número {v}')
    
print('Posições:')

c = 1
for k in sorted(jogadores, key=jogadores.get):
    print(f'{c}º posição: {k}')
    c+=1
    
# Sorted para ordenar dicionario para o maior valor em primeiro lugar