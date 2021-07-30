# Funções
from datetime import datetime

def voto(ano):
    ano_atual = datetime.now().year
    idade = ano_atual - ano
    print(idade)
    
    if idade >= 65:
        return 'Voto OPCIONAL'
    elif idade >= 18:
        return 'Voto OBRIGATORIO'
    elif idade < 18:
        return 'Voto NÃO OBRIGATORIO'
    

print(voto(int(input('Ano de nascimento: '))))