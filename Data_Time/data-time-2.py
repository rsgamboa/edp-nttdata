from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = '2023-12-31 23:59'
mascara_ptbr = '%d/%m/%Y %a'
mascara_en = '%Y-%m-%d %a'

print(data_hora_atual.strftime(mascara_ptbr))

print(datetime.strftime(data_hora_atual, mascara_en))