from datetime import datetime, timedelta

# strptime(str, fmt)
# .strftime(fmt)
# timestamp
# fromtimestamp()

data = datetime.strptime('17/08/2022', '%d/%m/%Y')
data = data + timedelta(days=5, seconds=59)
print(data)
