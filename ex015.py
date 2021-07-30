# Funções

def maior(*numbers):
    mai = 0
    for i in numbers:
        if i > mai:
            mai = i
    print(f'Dos valores {numbers}, o maior valor é {mai}.')
    
maior(2,79,3546,356,)

# max() pode ser usado