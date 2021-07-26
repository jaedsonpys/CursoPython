alunos = []

while True:
    nome = str(input('Nome: ')).strip()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    
    media = nota1 + nota2 / 2
    aluno = [nome, nota1, nota2, media]
    alunos.append(aluno)
    
    cont = str(input('Quer continuar? [s/n] ')).strip().lower()
    if cont == 's':
        continue
    elif cont == 'n':
        break
    
for c, aluno in enumerate(alunos):
    print('\n======================')
    print(f'\nAluno {c}\n')
    print(f'Nome: {str(aluno[0]).capitalize()}')
    print(f'Média: {str(aluno[3])}')
    print(f'ID: {c}')
    
while True:
    Id = int(input('Qual aluno deseja ver? (999 para sair) '))

    if Id != 999:
        print('\n=========================')
        print(f'{alunos[Id][0]}')
        print(f'Notas: {alunos[Id][1]}, {alunos[Id][2]}')
    else:
        print('Adeus')
        break