matriz = []

for i in range(3):
    line = []
    for p in range(3):
        num = int(input(f'Digite um número [{i}, {p}]: '))
        line.append(num)
    matriz.append(line)
    
print()
for lines in matriz:
    print(lines)