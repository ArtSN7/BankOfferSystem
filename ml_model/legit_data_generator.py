import csv
import random
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

with open('data/legit_data.csv', 'w', newline='') as csvfile:
    user = csv.writer(csvfile,
                      quotechar=',', quoting=csv.QUOTE_MINIMAL)
    user.writerow(['business_types', 'legal_form',
                   'authorized_capital(thousands)', 'revenue(millions)', 'net_profit(millions)', 'from'])
    for i in range(1, 10001):
        revenue = random.randint(1, 100000)
        user.writerow([random.randint(1, 21),
                       random.randint(1, 6),
                       random.randint(1, 990000),
                       revenue,
                       revenue * random.random(),
                       random.randint(0, 48)])
