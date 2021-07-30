# Funções

def jogo(nome, gols):
    if gols == '':
        gols = 0
    else:
        gols = int(gols)
    if nome == '':
        nome = '<desconhecido>'
    print(f'O jogador {nome} fez {gols} gol(s).')
    

jogo(str(input('Nome: ')), str(input('Gols: ')))