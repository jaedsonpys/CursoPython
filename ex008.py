# Cire um programa que leia nome, ano de nascimento e carteira de trabalho e os cadastre (com idade)
# em um dicionario. Se por acaso a CTPS fo diferente de zero, o dicionario tambem receberá o ano de
# contratação e o salário. Calcule e acrescente, alem da idade, com quantos anos a pessoa vai se aposentar

from datetime import datetime

nome = str(input('Nome: ')).strip()
nasc = int(input('Ano de nascimento: '))
ctps = int(input('Carteira de trabalho: '))

ano = datetime.now().year
idade = ano - nasc

pessoa = {
    'nome': nome,
    'carteira': ctps,
    'idade': idade
}

if ctps != 0:
    ctr = int(input('Ano de contratação: '))
    slr = float(input('Salário: '))
    aps = ctr + 35
    pessoa['aposentadoria'] = aps
    pessoa['salario'] = slr
    pessoa['ctr'] = ctr
    
print(f'Nome da pessoa: {pessoa["nome"]}') 
print(f'Idade: {pessoa["idade"]}')   
print(f'Carteira: {pessoa["carteira"]}')
if pessoa['carteira'] != 0:
    print(f'Salário: {pessoa["salario"]}')
    print(f'Ano de contratação: {pessoa["ctr"]}')
    print(f'Ano de aposentadoria: {pessoa["aposentadoria"]}')