matriz = []
isPar = 0
sColumn = 0
mai = 0

for i in range(3):
    line = []
    for p in range(3):
        num = int(input(f'Digite um número [{i}, {p}]: '))
        line.append(num)
        if num % 2 == 0:
            isPar += num
        if i == 1:
            if num > mai:
                mai = num
    matriz.append(line)
    
print()
for i, lines in enumerate(matriz):
    for c in lines:
        print(f'[{c}]', end='')
        if i == 2:
            sColumn += c
    print()
print(f'A soma de todos os valores pares são {isPar}')
print(f'A soma dos valores da terceira coluna são: {sColumn}')
print(f'O maior valor da segunda coluna é: {mai}')