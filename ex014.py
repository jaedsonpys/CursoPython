# Funções

def cont(inicio, fim, passo):
    print('-='*30)
    print(f'Iniciando contagem de {inicio} até {fim} de {passo} em {passo}.')
    if passo == 0:
        passo = 1
    if passo > fim:
        passo = 1
    while True:
        if inicio > fim:
            inicio -= passo
        elif inicio < fim:
            inicio += passo
        else:
            break
        print(inicio, end=' ')
    print('FIM')
    print('-='*30)
    
    
cont(10, -5, 1)
cont(0,100, 2)

print('Sua vez: ')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
cont(inicio, fim, passo)