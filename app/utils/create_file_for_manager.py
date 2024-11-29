# делаем файл со всеми лидами

import sqlite3
import pandas as pd

def get_leads_by_manager_id(manager_id):
    # Connect to the SQLite database
    conn = sqlite3.connect("hack_db_mvp.db")
    cursor = conn.cursor()

    # Query to get leads by manager_id and join with other tables
    query = f"""
    SELECT
        l.*,
        c.client_name, c.client_middle_name, c.client_sirname, c.client_birthdate, c.client_birthplace, c.client_mobile_phone, c.client_education,
        p.passport_series, p.passport_number, p.passport_issue_date, p.passport_issue_place, p.passport_issue_code, p.passport_no_previous,
        z.zagran_passport_series, z.zagran_passport_number, z.zagran_passport_issue_date, z.zagran_passport_issue_place, z.zagran_passport_issue_code,
        d.driver_license_series, d.driver_license_number, d.driver_license_issue_date, d.driver_license_issue_place, d.driver_license_issue_code,
        cr.credit_sum, cr.credit_term, cr.credit_initial, cr.credit_dog_issue_date,
        f.client_family_status, f.client_children_dependents,
        r.client_registration_address, r.client_registration_own_type, r.client_registration_date,
        j.job_type, j.workplace_name, j.workplace_inn, j.workplace_client_position, j.workplace_address, j.workplace_phone, j.workplace_workdate, j.workplace_work_experience, j.workplace_income_amount, j.workplace_additional_income_amount, j.workplace_additional_income_type,
        ca.car_brand, ca.car_model, ca.car_year, ca.car_price, ca.car_dop_price, ca.car_type, ca.car_condition, ca.car_transmission, ca.car_mileage
    FROM
        leads_table l
    LEFT JOIN
        clients c ON l.client_id = c.id
    LEFT JOIN
        passports p ON l.client_id = p.client_id
    LEFT JOIN
        zagran_passports z ON l.client_id = z.client_id
    LEFT JOIN
        driver_licenses d ON l.client_id = d.client_id
    LEFT JOIN
        credits cr ON l.client_id = cr.client_id
    LEFT JOIN
        family_info f ON l.client_id = f.client_id
    LEFT JOIN
        registration_info r ON l.client_id = r.client_id
    LEFT JOIN
        job_info j ON l.client_id = j.client_id
    LEFT JOIN
        car_info ca ON l.client_id = ca.client_id
    WHERE
        l.manager_id = {manager_id}
    """

    # Execute the query and fetch the results
    cursor.execute(query)
    rows = cursor.fetchall()

    # Get column names from the cursor description
    column_names = [description[0] for description in cursor.description]

    # Close the connection
    conn.close()

    # Create a DataFrame from the fetched data
    df = pd.DataFrame(rows, columns=column_names)

    return df

def save_to_excel(df, output_file):
    # Save the DataFrame to an Excel file
    df.to_excel(output_file, index=False)


def main_calling_func(manager_id, output_file):
    # Get the leads data for the specified manager_id
    leads_df = get_leads_by_manager_id(manager_id)

    # Save the data to an Excel file
    save_to_excel(leads_df, output_file)


# main_calling_func(1, "test.xlsx") - example
