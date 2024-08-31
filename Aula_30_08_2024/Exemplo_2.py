'''def exibir_intervalo(ini=0, fim=20, passo=5):
    for item in range(ini,fim,passo):
        print(item)
        
exibir_intervalo(0,20,5)
exibir_intervalo(fim = 5, passo = 5)'''

def exibir_valores(*valores):
    for valor in valores:
        print(valor)
        
exibir_valores(10,20,30)