from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

data_atual = datetime.now()

ano_atual = data_atual.year
mes_atual = data_atual.month
dia_atual = data_atual.day

print(f"Data atual: {data_atual}")
print(f"Ano atual: {ano_atual}")
print(f"Mês atual: {mes_atual}")
print(f"Dia atual: {dia_atual}")
print(f"Data atual formatada: {dia_atual}/{mes_atual}/{ano_atual}")


data_extenso = data_atual.strftime('%d de %B de %Y')
print(f"Data por extenso: {data_extenso}")
