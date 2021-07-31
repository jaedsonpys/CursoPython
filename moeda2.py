def metade(num, view=False):
    if view:
        return f'R${num / 2}'
    else:
        return num / 2


def dobro(num, view=False):
    if view:
        return f'R${num * 2}'
    else:
        return num * 2


def aumentar(num, porc, view=False):
    new = (porc / 100) * num
    if view:
        return f'R${num + new}'
    else:
        return num + new


def diminur(num, porc, view=False):
    new = (porc / 100) * num
    if view:
        return f'R${num - new}'
    else:
        return num - new
    

def resumo(num, aum, dim):
    print('-=' * 30)
    print(f'Tabela de valores')
    print('-=' * 30)
    print(f'Valor informado: {num}')
    print(f'Dobro de {num}: {dobro(num)}')
    print(f'Metade de {num}: {metade(num)}')
    print(f'Aumentar {aum}% de {num}: {aumentar(num, aum)}')
    print(f'Diminuir {dim}% de {num}: {diminur(num, dim)}')
    print('-=' * 30)