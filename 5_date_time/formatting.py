from datetime import datetime

date_time = datetime.now()
print(date_time)
mask_br = "%d/%m/%Y %a"
mask_en = "%Y-%m-%d %H:%M"
date_str = "2025-12-01 13:27"

print(date_time.strftime(mask_br))
date_formatting = datetime.strptime(date_str, mask_en)
print(date_formatting)
print(type(date_formatting))
