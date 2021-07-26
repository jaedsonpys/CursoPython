# Cire um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
# em um dicionario e todos os dicionarios em uma lista, No final, mostre:
# a) Quantas pessoas foram cadastradas
# b) A média de idade do grupo
# c) Uma lista com todas as mulheres
# d) Uma lista com todas as pessoas acima da media

listaPessoas = []

while True:
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).lower()

    while sexo not in 'mf':
        sexo = str(input('Sexo: [M/F] ')).lower()

    pessoa = {'nome': nome, 'idade': idade, 'sexo': str(sexo).upper()}
    listaPessoas.append(pessoa)

    cnt = str(input('Quer continuar? [S/N] ')).lower()
    
    while cnt not in 'sn':
        cnt = str(input('Quer continuar? [S/N] ')).lower()
    
    if cnt == 'n':
        break
    
print('-='*30)
print(f'No total, {len(listaPessoas)} foram cadastradas.')

idades = 0
female = []
for people in listaPessoas:
    idades += people['idade']
    if people['sexo'] == 'F':
        female.append(people['nome'])
        
iMedia = idades / len(listaPessoas)

acimaDaMedia = []
for people in listaPessoas:
    if people['idade'] > int(iMedia):
        acimaDaMedia.append(people['nome'])

print(f'A média de todas as idades são {int(iMedia)}')
print(f'Todas as mulheres cadastradas: {female}')
print(f'As pessoas acima da média de idade são: {acimaDaMedia}')
