import sqlite3
from datetime import date


def add_to_leads():

    conn = sqlite3.connect('hack_db_mvp.db') # connect to the DB
    cursor = conn.cursor()

    result = cursor.execute("""SELECT * FROM final_table""").fetchall()
    for obj in result:

        user_id, comp, service, prob = obj

        dictt = {"Экспобанк": 1, "Автоэкспресс": 3, "Д2 страхование": 2, "EXPOCAR": 4, "Парк-отель Хвоя": 5, "Лизинг 1 ( операционный и финансовый лизинг)": 6}

        manager_id = dictt[comp]

        cursor.execute('''INSERT INTO leads_table (client_id, manager_id, company_name_to, company_name_from, cross_stuff, date_of_recieve, rate_of_lead, is_complete)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                       (user_id, manager_id, comp, "Экспобанк", service, date.today(), prob, False))
        
    conn.commit()




add_to_leads()