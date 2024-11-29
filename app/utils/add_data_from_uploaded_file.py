# function that adds new clients to the relevant tables in the DB

# STEP 1 - загружаем из файла в базу данных и идем на степ 2

import pandas as pd
import sqlite3


def getting_last_id_in_clients():
    try:
        conn = sqlite3.connect('hack_db_mvp.db') # connect to the DB
        cur = conn.cursor()
        result = cur.execute("""SELECT id FROM clients""").fetchall() # getting all the ID's in the final table

        return result[-1][0]
    
    except Exception as e:
        print(e)
        return 0


# main function that opens file
def open_file(name_of_the_file): # file must be .xls or .xlsx 

    file_path = name_of_the_file # name_of_the_file

    print("SUCCCEKASDMS<DM<ADSAMDm")

    df = pd.read_excel(file_path)

    data_list = df.values.tolist()

    for row in data_list: # adding each row ( client ) into db

        print(row)

        add_to_tables(row)


# function that adds to table
def add_to_tables(data):

    conn = sqlite3.connect('hack_db_mvp.db') # connect to the DB
    cursor = conn.cursor()

    client_id = getting_last_id_in_clients() + 1

    print(client_id)


    cursor.execute('''INSERT INTO clients (client_name, client_middle_name, client_sirname, client_birthdate, client_birthplace, client_mobile_phone, client_education)
                   VALUES (?, ?, ?, ?, ?, ?, ?)''',
                    (data[1], data[2], data[3], data[4].date(), data[5], data[6], data[10]))
    
    cursor.execute('''INSERT INTO passports (client_id, passport_series, passport_number, passport_issue_date, passport_issue_place, passport_issue_code, passport_no_previous)
                   VALUES (?, ?, ?, ?, ?, ?, ?)''',
                    (client_id, data[11], data[12], data[13].date(), data[14], data[15], data[16]))
    
    cursor.execute('''INSERT INTO zagran_passports (client_id, zagran_passport_series, zagran_passport_number, zagran_passport_issue_date, zagran_passport_issue_place, zagran_passport_issue_code)
                   VALUES (?, ?, ?, ?, ?, ?)''',
                   (client_id, data[17], data[18], data[19].date(), data[20], data[21]))
    
    cursor.execute('''INSERT INTO driver_licenses (client_id, driver_license_series, driver_license_number, driver_license_issue_date, driver_license_issue_place, driver_license_issue_code)
                   VALUES (?, ?, ?, ?, ?, ?)''',
                    (client_id, data[22], data[23], data[24].date(), data[25], data[26]))
    
    cursor.execute('''INSERT INTO credits (client_id, credit_sum, credit_term, credit_initial, credit_dog_issue_date)
                   VALUES (?, ?, ?, ?, ?)''',
                    (client_id, data[27], data[28], data[29], data[30].date()))
    
    cursor.execute('''INSERT INTO family_info (client_id, client_family_status, client_children_dependents) 
                   VALUES (?, ?, ?)''', (client_id, data[31], data[32]))

    cursor.execute('''INSERT INTO registration_info (client_id, client_registration_address, client_registration_own_type, client_registration_date)
                   VALUES (?, ?, ?, ?)''',
                    (client_id, data[33], data[34], data[35].date()))
    
    cursor.execute('''INSERT INTO job_info (client_id, job_type, workplace_name, workplace_inn, workplace_client_position, workplace_address, workplace_phone, workplace_workdate, workplace_work_experience, workplace_income_amount, workplace_additional_income_amount, workplace_additional_income_type)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    (client_id, data[36], data[37], data[38], data[39], data[40], data[41], data[42].date(), data[43], data[44], data[45], data[46]))
    
    cursor.execute('''INSERT INTO car_info (client_id, car_brand, car_model, car_year, car_price, car_dop_price, car_type, car_condition, car_transmission, car_mileage)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    (client_id, data[47], data[48], data[49], data[50], 0.0, "zaglushka", "zaglushka", "zaglushka", "zaglushka"))
    
    conn.commit()