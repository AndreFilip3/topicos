# Exercício 7
from datetime import datetime

data_atual = datetime.now()
print("Data atual:", data_atual)
print("Ano atual:", data_atual.year)
print("Mês atual:", data_atual.month)
print("Dia atual:", data_atual.day)
print("Data atual formatada:", data_atual.strftime("%d/%m/%Y"))
print("Data atual no formato:", data_atual.strftime("%d de %B de %Y"))