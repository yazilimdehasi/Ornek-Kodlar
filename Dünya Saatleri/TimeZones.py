import pytz

from datetime import datetime

ist = pytz.timezone('Europe/Istanbul')

nw = pytz.timezone('America/New_York')

lnd = pytz.timezone('Europe/London')
print()
print('Istanbul Saati : ', datetime.now(tz=ist))
print('New York Saati : ', datetime.now(tz=nw))
print('Londra Saati : ', datetime.now(tz=lnd))




