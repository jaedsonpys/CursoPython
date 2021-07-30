# Funções

def leia(msg):
    value = str(input(msg))
    while True:
        if value.isnumeric():
            return int(value)
        else:
            print('Erro, digite um número')
            value = str(input(msg))
    
n = leia('Digite um número: ')
print(f'Você digitou o número {n}')