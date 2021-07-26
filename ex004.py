from random import randint
from time import sleep

print('+=' * 15)
print('{:^30}'.format('Sorteio'))
print('+=' * 15)

nas = int(input('Quantos numeros você deseja sortear? '))

for i in range(nas):
    count = 0
    game = list()
    while True:
        number = randint(0, 60)
        if number not in game:
            game.append(number)
        if count >= 6:
            break
        count += 1
    print(f'Seu jogo é: {game}')

    
print('\n+=+=+=+= Boa sorte +=+=+=+=')