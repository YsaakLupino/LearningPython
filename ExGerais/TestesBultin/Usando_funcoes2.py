vendas  = 100

def calcular_imposto(vendas:int = 100):
    if vendas > 50:
        imposto = vendas * 0.5
    elif vendas > 25:
        imposto = vendas * 0.25
    else: 
        imposto = 0

    
    return imposto

print(calcular_imposto())