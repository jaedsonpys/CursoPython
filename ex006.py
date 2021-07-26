# Faça um programa que leia o nome e a média de um aluno,
# guardando também a situação em um dicionário. No final, mostre a estrutura na tela

aluno = {}

nome = str(input('Nome: ')).strip()
média = float(input('Média: '))

if média >= 5:
    status = 'aprovado'
else:
    status = 'reprovado'

aluno['nome'] = nome
aluno['media'] = média
aluno['status'] = status

print('-=' * 30)

print(f'Nome do aluno: {aluno["nome"]}')
print(f'Média do aluno: {aluno["media"]}')
print(f'Status do aluno: {aluno["status"]}')
print('\nFim\n')