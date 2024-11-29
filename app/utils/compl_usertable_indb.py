#function that will add NEW USERS THAT HAS BEEN UPLOADED into table called user_table ( for ML ) in our DB 

# STEP 2 NAHUY - вызываем функцию и она переносит всех новыъ пользователей в user_table для МЛ

# МЛ берет данные из user_table и предсказания выдаются в final_table 

import sqlite3
import datetime
from dateutil.relativedelta import relativedelta



conn = sqlite3.connect('hack_db_mvp.db') # connect to the DB
cur = conn.cursor()




def getting_last_id_in_usertable():
    try:

        result = cur.execute("""SELECT client_id FROM user_data""").fetchall() # getting all the ID's in the final table

        return result[-1][0]
    
    except Exception as e:
        return 0



# function that fill the user table with the new users
def filling_user_table():

    starting_id = getting_last_id_in_usertable() # getting the id of the last written user to the final table

    result = cur.execute("""SELECT id FROM clients WHERE id > ?""", (starting_id, )).fetchall() # getting all the ID's of users that are not in the final table

    for elem in result: # for every new user to add

        # getting all valid fields from tables
 
        user_id = elem[0]

        age = calc_age(user_id)

        zagran_passport = cur.execute("""SELECT zagran_passport_series FROM zagran_passports WHERE client_id = ?""", (user_id, )).fetchall()[0][0]

        if zagran_passport is None:
            zagran_passport = False
        else: zagran_passport = True 

        driver_license = cur.execute("""SELECT driver_license_series FROM driver_licenses WHERE client_id = ?""", (user_id, )).fetchall()[0][0]

        if driver_license is None:
            driver_license = False
        else: driver_license = True 

        credit_sum = calc_credit_sum(user_id)

        family_status = cur.execute("""SELECT client_family_status FROM family_info WHERE client_id = ?""", (user_id, )).fetchall()[0][0]
        
        children_dependents = cur.execute("""SELECT client_children_dependents FROM family_info WHERE client_id = ?""", (user_id, )).fetchall()[0][0]

        work_exp = cur.execute("""SELECT workplace_work_experience FROM job_info WHERE client_id = ?""", (user_id, )).fetchall()[0][0]

        income = cur.execute("""SELECT workplace_income_amount FROM job_info WHERE client_id = ?""", (user_id, )).fetchall()[0][0]

        add_income = cur.execute("""SELECT workplace_additional_income_amount FROM job_info WHERE client_id = ?""", (user_id, )).fetchall()[0][0]

        add_income_type = cur.execute("""SELECT workplace_additional_income_type FROM job_info WHERE client_id = ?""", (user_id, )).fetchall()[0][0]

        car_price = cur.execute("""SELECT car_price FROM car_info WHERE client_id = ?""", (user_id, )).fetchall()[0][0]

        # adding to the user table

        cur.execute('''INSERT INTO user_data (client_id, age, zagran_passport, driver_license, credit_sum, family_status, children_dependents, work_experience, income, additional_income, additional_income_type, car_price)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                    (user_id, age, zagran_passport, driver_license, credit_sum, family_status, children_dependents, work_exp, income, add_income, add_income_type, car_price))
        conn.commit()
    

    conn.close()




# function to calculate the age of the client
def calc_age(user_id): 
    birthdate = cur.execute("""SELECT client_birthdate FROM clients WHERE id = ?""", (user_id, )).fetchall()[0][0]

    birthdate = datetime.datetime.strptime(birthdate, '%Y-%m-%d').date()
    today = datetime.date.today()
    age = relativedelta(today, birthdate).years

    return age


# function to calculate the total amount of the credit sum
def calc_credit_sum(user_id):

    count = 0 # sum of credits

    data = cur.execute("""SELECT credit_sum FROM credits WHERE client_id = ?""", (user_id, )).fetchall()

    for el in data:
        count += el[0]

    return count


# calling this function for the test
filling_user_table() 