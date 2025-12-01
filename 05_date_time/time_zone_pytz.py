import pytz
from datetime import datetime

date = datetime.now(pytz.timezone('US/Eastern'))

print(date)