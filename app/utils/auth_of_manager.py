import sqlite3
from typing import Optional


def getting_response_of_auth(email: str, password: str) -> Optional[dict]:
    """
    This function is called during authentication of the manager and checks
    if the provided password matches the stored password in the database.
    If the credentials are valid, it returns a dictionary containing
    the user's ID and manager's name. If the credentials are invalid, it returns None.
    """
    conn = sqlite3.connect('hack_db_mvp.db')
    cur = conn.cursor()

    query = "SELECT id, password, manager_name FROM managers_table WHERE email = ?"
    cur.execute(query, (email,))
    result = cur.fetchone()
    conn.close()

    if result is None:
        return None

    user_id, stored_password, manager_name = result

    if stored_password == password:
        return {'id': user_id, 'manager_name': manager_name}
    return None
