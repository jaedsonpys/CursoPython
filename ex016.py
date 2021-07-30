# Funções

from random import randint

def sumPar(lst):
    res = 0
    for i in lst:
        if i % 2 == 0:
            res += i
            
    print(f'A soma dos valores pares são: {res}')

def sort():
    numbers = [randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)]
    print(f'Os valores sorteados foram: {numbers}')
    sumPar(numbers)
    
sort()
sort()
sort()
