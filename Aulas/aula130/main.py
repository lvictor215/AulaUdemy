from datetime import datetime
from locale import setlocale, LC_ALL

setlocale(LC_ALL, 'pt_BR.utf-8')

data = datetime(2019, 4, 20, 10, 53, 20)

formatado = data.strftime('%H:%M:%S do dia %d de %B de %Y')
print(formatado)



