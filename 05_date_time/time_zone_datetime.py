from datetime import datetime, timezone, timedelta

data_oslo = datetime.now(timezone(timedelta(hours=2), "OSLO"))
data_brt = datetime.now(timezone(timedelta(hours=-3), "BRT"))

print(data_oslo)
print(data_brt)