import moeda

num = int(input('Digite um número: '))

print(f'O dobro de {num} é {moeda.dobro(num)}')
print(f'A metade de {num} é {moeda.metade(num)}')
print(f'Aumentando 35% de {num}, o novo valor é de {moeda.aumentar(num, 35, view=True)}')
print(f'Descontando 15% de {num}, o novo valor é de {moeda.diminur(num, 15, view=True)}')