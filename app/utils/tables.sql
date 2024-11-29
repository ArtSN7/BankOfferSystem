-- Next tables are 3NF of hackaton_client_data table:

-- Create clients table
CREATE TABLE clients (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  client_name TEXT DEFAULT NULL,
  client_middle_name TEXT DEFAULT NULL,
  client_sirname TEXT DEFAULT NULL,
  client_birthdate DATE DEFAULT NULL,
  client_birthplace TEXT DEFAULT NULL,
  client_mobile_phone TEXT DEFAULT NULL,
  client_education TEXT DEFAULT NULL
);

-- Create passports table
CREATE TABLE passports (
  client_id INTEGER PRIMARY KEY DEFAULT NULL,
  passport_series TEXT DEFAULT NULL,
  passport_number TEXT DEFAULT NULL,
  passport_issue_date DATE DEFAULT NULL,
  passport_issue_place TEXT DEFAULT NULL,
  passport_issue_code TEXT DEFAULT NULL,
  passport_no_previous INTEGER DEFAULT NULL,
  FOREIGN KEY (client_id) REFERENCES clients(id)
);

-- Create zagran_passports table
CREATE TABLE zagran_passports (
  client_id INTEGER PRIMARY KEY,
  zagran_passport_series TEXT DEFAULT NULL,
  zagran_passport_number TEXT DEFAULT NULL,
  zagran_passport_issue_date DATE DEFAULT NULL,
  zagran_passport_issue_place TEXT DEFAULT NULL,
  zagran_passport_issue_code TEXT DEFAULT NULL,
  FOREIGN KEY (client_id) REFERENCES clients(id)
);


-- Create driver_licenses table
CREATE TABLE driver_licenses (
  client_id INTEGER PRIMARY KEY,
  driver_license_series TEXT DEFAULT NULL,
  driver_license_number TEXT DEFAULT NULL,
  driver_license_issue_date DATE DEFAULT NULL,
  driver_license_issue_place TEXT DEFAULT NULL,
  driver_license_issue_code TEXT DEFAULT NULL,
  FOREIGN KEY (client_id) REFERENCES clients(id)
);

-- Create credits table
CREATE TABLE credits (
  client_id INTEGER PRIMARY KEY,
  credit_sum REAL DEFAULT NULL,
  credit_term INTEGER DEFAULT NULL,
  credit_initial REAL DEFAULT NULL,
  credit_dog_issue_date DATE DEFAULT NULL,
  FOREIGN KEY (client_id) REFERENCES clients(id)
);

-- Create family_info table
CREATE TABLE family_info (
  client_id INTEGER PRIMARY KEY,
  client_family_status TEXT DEFAULT NULL,
  client_children_dependents INTEGER DEFAULT NULL,
  FOREIGN KEY (client_id) REFERENCES clients(id)
);

-- Create registration_info table
CREATE TABLE registration_info (
  client_id INTEGER PRIMARY KEY,
  client_registration_address TEXT DEFAULT NULL,
  client_registration_own_type TEXT DEFAULT NULL,
  client_registration_date DATE DEFAULT NULL,
  FOREIGN KEY (client_id) REFERENCES clients(id)
);

-- Create job_info table
CREATE TABLE job_info (
  client_id INTEGER PRIMARY KEY,
  job_type TEXT DEFAULT NULL,
  workplace_name TEXT DEFAULT NULL,
  workplace_inn TEXT DEFAULT NULL,
  workplace_client_position TEXT DEFAULT NULL,
  workplace_address TEXT DEFAULT NULL,
  workplace_phone TEXT DEFAULT NULL,
  workplace_workdate DATE DEFAULT NULL,
  workplace_work_experience INTEGER DEFAULT NULL,
  workplace_income_amount REAL DEFAULT NULL,
  workplace_additional_income_amount REAL DEFAULT NULL,
  workplace_additional_income_type TEXT DEFAULT NULL,
  FOREIGN KEY (client_id) REFERENCES clients(id)
);

-- Create car_info table
CREATE TABLE car_info (
  client_id INTEGER PRIMARY KEY,
  car_brand TEXT DEFAULT NULL,
  car_model TEXT DEFAULT NULL,
  car_year INTEGER DEFAULT NULL,
  car_price REAL DEFAULT NULL,
  car_dop_price REAL DEFAULT NULL,
  car_type TEXT DEFAULT NULL,
  car_condition TEXT DEFAULT NULL,
  car_transmission TEXT DEFAULT NULL,
  car_mileage TEXT DEFAULT NULL,
  FOREIGN KEY (client_id) REFERENCES clients(id)
);

------------------
-- end of 3NF

-- Create user_data table
CREATE TABLE user_data (
  client_id INTEGER PRIMARY KEY,
  age INTEGER DEFAULT NULL,
  zagran_passport BOOLEAN DEFAULT FALSE,
  driver_license BOOLEAN DEFAULT FALSE,
  credit_sum REAL DEFAULT NULL,
  family_status INTEGER DEFAULT NULL,
  children_dependents INTEGER DEFAULT NULL,
  work_experience INTEGER DEFAULT NULL,
  income REAL DEFAULT NULL,
  additional_income REAL DEFAULT NULL,
  additional_income_type INTEGER DEFAULT NULL,
  car_price REAL DEFAULT NULL,
  FOREIGN KEY (client_id) REFERENCES clients(id)
);

-- Create final_table
CREATE TABLE final_table (
  user_id INTEGER,
  company_name TEXT DEFAULT NULL,
  relevant_service_1 TEXT DEFAULT NULL,
  probability_1 REAL DEFAULT NULL,
  FOREIGN KEY (user_id) REFERENCES clients(id)
);


-- table с лидами
CREATE TABLE leads_table (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  client_id INTEGER DEFAULT NULL,
  manager_id INTEGER DEFAULT NULL,
  company_name_to TEXT DEFAULT NULL,
  company_name_from TEXT DEFAULT NULL,
  cross_stuff TEXT DEFAULT NULL,
  date_of_recieve DATE DEFAULT NULL,
  rate_of_lead REAL DEFAULT NULL,
  is_complete BOOLEAN DEFAULT FALSE
);

CREATE TABLE managers_table (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  manager_name TEXT DEFAULT NULL,
  company_name TEXT DEFAULT NULL,
  email TEXT DEFAULT NULL,
  password TEXT DEFAULT NULL
)

