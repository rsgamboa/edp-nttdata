import pytz
from datetime import datetime

# Cria um objeto timezone
tz = pytz.timezone('Europe/Oslo') 

# Cria um objeto datetime
data_hora_atual = datetime.now(tz)

print(data_hora_atual)