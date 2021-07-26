# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
# e quantas partidas ele jogou, Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo será mostrado
# em um dicionário, incluindo o total de gols feitos durante o campeonato.

gols = []
jogador = {}

nome = str(input('Nome do jogador: '))
partidas = int(input('Quantidade de partidas: '))

total = 0
for i in range(partidas):
    gol = int(input(f'Quantos gols ele fez na partida {i+1}? '))
    total += gol
    gols.append(gol)
    
jogador['nome'] = nome
jogador['partidas'] = partidas
jogador['gols'] = gols
jogador['total'] = total

print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas e fez um total de {jogador["total"]} gols.')
print('-='*30)

mai = 0
pos = ''
for c, g in enumerate(jogador['gols']):
    if g == 0:
        print(f'Na partida {c + 1}º, {jogador["nome"]} não fez nenhum gol.')
    else:
        print(f'Na partida {c + 1}º, {jogador["nome"]} fez {g} gols')
    if g > mai:
        mai = g
        pos = c
        
print('-='*30)
print(f'A maior quantidade de gols do jogador {jogador["nome"]} foi na partida {pos}º')