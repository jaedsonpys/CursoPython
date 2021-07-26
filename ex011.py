# Aprimore o desafio 09 para que ele funcione para vários jogadores, incluindo um sistema de visualização de
# detalhes do aproveitamento de cada jogador

jogadores = []

while True:
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
    jogadores.append(jogador)
    
    ctn = str(input('Quer continuar? [S/N] ')).lower()
    
    while ctn not in 'sn':
        ctn = str(input('Quer continuar? [S/N] ')).lower()
        
    if ctn == 'n':
        break
    
    
print('-='*30)
print('{:^10} | {:^10}'.format('ID', 'Nome'))
for jg in jogadores:
    print(f'{jogadores.index(jg):^10} | {jg["nome"]:^10}')
print('-='*30)


while True:
    try:
        choose = int(input('Qual jogador você quer ver? '))
        if choose == 999:
            break
        jogadores[choose]
    except:
        print('Erro, esse jogador não existe ou o valor não é um número.')
    else:
        print('-='*30)
        print(f'O jogador {jogadores[choose]["nome"]} jogou {jogadores[choose]["partidas"]} partidas e fez um total de {jogadores[choose]["total"]} gols.')
        mai = 0
        pos = ''
        for c, g in enumerate(jogadores[choose]['gols']):
            if g == 0:
                print(f'Na partida {c + 1}º, {jogadores[choose]["nome"]} não fez nenhum gol.')
            else:
                print(f'Na partida {c + 1}º, {jogadores[choose]["nome"]} fez {g} gols')
            if g > mai:
                mai = g
                pos = c
        print(f'A maior quantidade de gols do jogador {jogadores[choose]["nome"]} foi na partida {pos}º')
        print('-='*30)
        
print('-='*30)
print('Fim do programa')