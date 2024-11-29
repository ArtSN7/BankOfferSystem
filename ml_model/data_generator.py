import csv
import random
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


def random_age(start_date, end_date):
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return relativedelta(datetime.now(), random_date).years


def car_price(driver_license):
    if not driver_license:
        return 0
    return random.randint(0, 1)


def children_dependents(family_status):
    if family_status == 2:
        return int(random.choices([0, 1], weights=[0.97, 0.03])[0])
    return int(random.choices([0, 1, 2, 3], weights=[0.3, 0.3, 0.2, 0.2])[0])


with open('data/phys_data.csv', 'w', newline='') as csvfile:
    user = csv.writer(csvfile,
                      quotechar=',', quoting=csv.QUOTE_MINIMAL)
    user.writerow(
        ['age', 'sex', 'zagran_passport', 'driver_license', 'credit_sum', 'family_status', 'children_dependents',
         'work_experience', 'income', 'additional_income', 'additional_income_type', 'car_price', 'from'
         ])
    for i in range(1, 10001):
        age = int(random.choices([random_age(datetime(1934, 1, 1), datetime(1943, 12, 31)),
                                  random_age(datetime(1944, 1, 1), datetime(1953, 12, 31)),
                                  random_age(datetime(1954, 1, 1), datetime(1973, 12, 31)),
                                  random_age(datetime(1974, 1, 1), datetime(1993, 12, 31)),
                                  random_age(datetime(1994, 1, 1), datetime(2005, 12, 31))],
                                 weights=[0.03, 0.15, 0.3, 0.38, 0.15])[0])
        income = int(random.choices([random.randint(20, 100),
                                     random.randint(101, 200),
                                     random.randint(201, 1000)],
                                    weights=[0.58, 0.4, 0.01])[0])
        add_income = int(random.choices([random.randint(0, 25),
                                         random.randint(26, 45),
                                         random.randint(46, 100),
                                         random.randint(101, 1000)],
                                        weights=[0.42, 0.32, 0.25, 0.01])[0])

        driver_license = int(random.choices([1, 0], weights=[0.6, 0.4])[0])
        family_status = int(random.choices([1, 2, 3, 4], weights=[0.5, 0.25, 0.15, 0.1])[0])

        user.writerow([age,
                       random.randint(1, 2),
                       int(random.choices([1, 0], weights=[0.4, 0.6])[0]),
                       driver_license,
                       int(random.choices([0, random.randint(50, 1000),
                                           random.randint(1001, 5000)], weights=[0.15, 0.7, 0.15])[0]),
                       family_status,
                       children_dependents(family_status),
                       int(age - 18 - (age - 18) * random.random()),
                       income,
                       add_income,
                       int(random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9])[0]),
                       int(car_price(driver_license) * (income + add_income) * random.randint(12, 36)),
                       random.randint(0, 51)])
