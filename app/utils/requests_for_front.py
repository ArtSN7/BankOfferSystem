import sqlite3
import random
import string


def get_user_data(manager_id: int | str) -> dict:
    user_data = {'id': manager_id}
    conn = sqlite3.connect('hack_db_mvp.db')
    cur = conn.cursor()

    query = "SELECT manager_name, company_name FROM managers_table WHERE id = ?"
    result = cur.execute(query, (manager_id,)).fetchall()[0]

    user_data['name'] = result[0]
    user_data['company'] = result[1]

    query = "SELECT id FROM leads_table WHERE manager_id = ?"
    result = cur.execute(query, (manager_id,)).fetchall()
    user_data['incoming_leads'] = len(result)
    user_data['outgoing_leads'] = 0

    conn.close()

    return user_data


def get_all_leads_data(manager_id: int | str) -> list[dict]:
    all_leads_data = []
    conn = sqlite3.connect('hack_db_mvp.db')
    cur = conn.cursor()

    query = "SELECT client_id, cross_stuff, date_of_recieve, rate_of_lead, is_complete FROM leads_table WHERE manager_id = ?"
    result_lead_table = cur.execute(query, (manager_id,)).fetchall()

    if not result_lead_table:
        return []

    for result_lead in result_lead_table:
        leads_data = {
            'user_id': result_lead[0],
            'cross_usluga': result_lead[1],
            'date_of_lead': result_lead[2],
            'rate_of_lead': result_lead[3],
            'is_complete': result_lead[4],
        }

        client_query = "SELECT client_name, client_middle_name, client_sirname, client_mobile_phone FROM clients WHERE id = ?"
        result = cur.execute(client_query, (leads_data['user_id'],)).fetchone()

        if result:
            leads_data['name'] = f"{result[0]} {result[1][0]}. {result[2][0]}."
            leads_data['phone_number'] = result[3]
            leads_data['email'] = generate_random_email("gmail.com")

        all_leads_data.append(leads_data)

    conn.close()
    return all_leads_data


def generate_random_string(length):
    """Generate a random string of fixed length."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def generate_random_email(domain="example.com"):
    """Generate a random email address."""
    username_length = random.randint(5, 10)
    username = generate_random_string(username_length)
    email = f"{username}@{domain}"
    return email


def request_for_fio(manager_id):
    conn = sqlite3.connect('hack_db_mvp.db')
    cur = conn.cursor()

    query = "SELECT manager_name FROM managers_table WHERE id = ?"
    result = cur.execute(query, (manager_id,)).fetchall()[0]

    return result[0]
