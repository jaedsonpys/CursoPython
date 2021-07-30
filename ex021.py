# Funções

def notas(*num, sit=False):
    maxvalue = max(num)
    minvalue = min(num)
    total = len(num)
    soma = sum(num)
    média = soma / total
    
    obj = {
        'total': total,
        'maxima': maxvalue,
        'minima': minvalue,
        'média': média,
    }
    
    if sit:
        if média > 7:
            obj['sit'] = 'Boa'
        elif média > 4:
            obj['sit'] = 'Razoavel'
        else:
            obj['sit'] = 'Ruim'    
            
    print(obj)
    
notas(7.3, 5.3, 2.4, sit=True)
notas(2.3,4.2, sit=True)