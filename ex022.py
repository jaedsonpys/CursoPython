# Funções

def pyhelp(element):
    print(f'Procurando por {element}')
    print(f'\033[32m{help(element)}\033[m')
    
while True:
    print('-='*20)
    print('SISTEMA DE AJUDA PYHELP')
    print('-='*20)
    pyhelp(str(input('Função ou biblioteca: ')))