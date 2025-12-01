from datetime import timedelta, date

data = date.today()
print(data)

calculo_sub = data - timedelta(days=10)
calculo_ad = data + timedelta(minutes=50000)

print(calculo_sub)
print(calculo_ad)