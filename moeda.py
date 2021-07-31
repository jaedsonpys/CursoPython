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