# rubbish function that was made to create a bullshit data to test tables in the fucking DB


import sqlite3
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Connect to the SQLite database
conn = sqlite3.connect('hack_db_mvp.db')
cursor = conn.cursor()

# Function to generate random date
def random_date(start_date, end_date):
    return fake.date_between(start_date=start_date, end_date=end_date)

# Function to insert data into clients table
def insert_clients(num_records):
    for _ in range(num_records):
        client_name = fake.first_name()
        client_middle_name = fake.first_name()
        client_sirname = fake.last_name()
        client_birthdate = random_date('-90y', '-18y')
        client_birthplace = fake.city()
        client_mobile_phone = fake.phone_number()
        client_education = random.choice(['High School', 'Bachelor', 'Master', 'PhD'])

        cursor.execute('''
            INSERT INTO clients (client_name, client_middle_name, client_sirname, client_birthdate, client_birthplace, client_mobile_phone, client_education)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (client_name, client_middle_name, client_sirname, client_birthdate, client_birthplace, client_mobile_phone, client_education))

# Function to insert data into passports table
def insert_passports(num_records):
    for client_id in range(1, num_records + 1):
        passport_series = fake.random_number(digits=4, fix_len=True)
        passport_number = fake.random_number(digits=6, fix_len=True)
        passport_issue_date = random_date('-30y', '-1y')
        passport_issue_place = fake.city()
        passport_issue_code = fake.random_number(digits=3, fix_len=True)
        passport_no_previous = random.choice([0, 1])

        cursor.execute('''
            INSERT INTO passports (client_id, passport_series, passport_number, passport_issue_date, passport_issue_place, passport_issue_code, passport_no_previous)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (client_id, passport_series, passport_number, passport_issue_date, passport_issue_place, passport_issue_code, passport_no_previous))

# Function to insert data into zagran_passports table
def insert_zagran_passports(num_records):
    for client_id in range(1, num_records + 1):
        zagran_passport_series = fake.random_number(digits=4, fix_len=True)
        zagran_passport_number = fake.random_number(digits=6, fix_len=True)
        zagran_passport_issue_date = random_date('-30y', '-1y')
        zagran_passport_issue_place = fake.city()
        zagran_passport_issue_code = fake.random_number(digits=3, fix_len=True)

        cursor.execute('''
            INSERT INTO zagran_passports (client_id, zagran_passport_series, zagran_passport_number, zagran_passport_issue_date, zagran_passport_issue_place, zagran_passport_issue_code)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (client_id, zagran_passport_series, zagran_passport_number, zagran_passport_issue_date, zagran_passport_issue_place, zagran_passport_issue_code))

# Function to insert data into driver_licenses table
def insert_driver_licenses(num_records):
    for client_id in range(1, num_records + 1):
        driver_license_series = fake.random_number(digits=4, fix_len=True)
        driver_license_number = fake.random_number(digits=6, fix_len=True)
        driver_license_issue_date = random_date('-30y', '-1y')
        driver_license_issue_place = fake.city()
        driver_license_issue_code = fake.random_number(digits=3, fix_len=True)

        cursor.execute('''
            INSERT INTO driver_licenses (client_id, driver_license_series, driver_license_number, driver_license_issue_date, driver_license_issue_place, driver_license_issue_code)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (client_id, driver_license_series, driver_license_number, driver_license_issue_date, driver_license_issue_place, driver_license_issue_code))

# Function to insert data into credits table
def insert_credits(num_records):
    for client_id in range(1, num_records + 1):
        credit_sum = fake.pyfloat(left_digits=5, right_digits=2, positive=True)
        credit_term = random.randint(1, 30)
        credit_initial = fake.pyfloat(left_digits=5, right_digits=2, positive=True)
        credit_dog_issue_date = random_date('-5y', 'today')

        cursor.execute('''
            INSERT INTO credits (client_id, credit_sum, credit_term, credit_initial, credit_dog_issue_date)
            VALUES (?, ?, ?, ?, ?)
        ''', (client_id, credit_sum, credit_term, credit_initial, credit_dog_issue_date))

# Function to insert data into family_info table
def insert_family_info(num_records):
    for client_id in range(1, num_records + 1):
        client_family_status = random.choice([1, 2, 3, 4])
        client_children_dependents = random.randint(0, 3)

        cursor.execute('''
            INSERT INTO family_info (client_id, client_family_status, client_children_dependents)
            VALUES (?, ?, ?)
        ''', (client_id, client_family_status, client_children_dependents))

# Function to insert data into registration_info table
def insert_registration_info(num_records):
    for client_id in range(1, num_records + 1):
        client_registration_address = fake.address()
        client_registration_own_type = random.choice(['Owned', 'Rented', 'Other'])
        client_registration_date = random_date('-30y', '-1y')

        cursor.execute('''
            INSERT INTO registration_info (client_id, client_registration_address, client_registration_own_type, client_registration_date)
            VALUES (?, ?, ?, ?)
        ''', (client_id, client_registration_address, client_registration_own_type, client_registration_date))

# Function to insert data into job_info table
def insert_job_info(num_records):
    for client_id in range(1, num_records + 1):
        job_type = random.choice(['Employed', 'Self-employed', 'Unemployed', 'Retired'])
        workplace_name = fake.company()
        workplace_inn = fake.random_number(digits=10, fix_len=True)
        workplace_client_position = fake.job()
        workplace_address = fake.address()
        workplace_phone = fake.phone_number()
        workplace_workdate = random_date('-30y', '-1y')
        workplace_work_experience = random.randint(0, 30)
        workplace_income_amount = fake.pyfloat(left_digits=5, right_digits=2, positive=True)
        workplace_additional_income_amount = fake.pyfloat(left_digits=5, right_digits=2, positive=True)
        workplace_additional_income_type = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])

        cursor.execute('''
            INSERT INTO job_info (client_id, job_type, workplace_name, workplace_inn, workplace_client_position, workplace_address, workplace_phone, workplace_workdate, workplace_work_experience, workplace_income_amount, workplace_additional_income_amount, workplace_additional_income_type)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (client_id, job_type, workplace_name, workplace_inn, workplace_client_position, workplace_address, workplace_phone, workplace_workdate, workplace_work_experience, workplace_income_amount, workplace_additional_income_amount, workplace_additional_income_type))

# Function to insert data into car_info table
def insert_car_info(num_records):
    for client_id in range(1, num_records + 1):
        car_brand = fake.random_element(elements=('Toyota', 'Honda', 'Ford', 'Chevrolet', 'BMW', 'Mercedes', 'Audi', 'Tesla'))
        car_model = fake.random_element(elements=('Model S', 'Model 3', 'Camry', 'Accord', 'Mustang', 'Corvette', 'X5', 'C-Class', 'A4', 'Model X'))
        car_year = random_date('-20y', '-1y')
        car_price = fake.pyfloat(left_digits=5, right_digits=2, positive=True)
        car_dop_price = fake.pyfloat(left_digits=5, right_digits=2, positive=True)
        car_type = random.choice(['Sedan', 'SUV', 'Coupe', 'Hatchback', 'Convertible'])
        car_condition = random.choice(['New', 'Used'])
        car_transmission = random.choice(['Manual', 'Automatic'])
        car_mileage = fake.random_number(digits=5, fix_len=True)

        cursor.execute('''
            INSERT INTO car_info (client_id, car_brand, car_model, car_year, car_price, car_dop_price, car_type, car_condition, car_transmission, car_mileage)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (client_id, car_brand, car_model, car_year, car_price, car_dop_price, car_type, car_condition, car_transmission, car_mileage))



# Insert data into tables
num_records = 100
insert_clients(num_records)
insert_passports(num_records)
insert_zagran_passports(num_records)
insert_driver_licenses(num_records)
insert_credits(num_records)
insert_family_info(num_records)
insert_registration_info(num_records)
insert_job_info(num_records)
insert_car_info(num_records)


# Commit the changes and close the connection
conn.commit()
conn.close()
