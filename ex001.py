expression = str(input('Digite sua expressão: ')).strip().lower()

while expression == '' or expression == None:
    expression = str(input('Digite sua expressão: ')).strip().lower()
    
pilha = list()
    
for letter in expression:
    if letter == '(':
        pilha.append('(')
    else:
        if len(pilha) > 0:
            pilha.pop()
        else:
            break
        
if len(pilha) == 0:
    print('Sua expressão está correta.')
else:
    print('Sua expressão está incorreta')