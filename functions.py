#used for clean project back-end code
import csv
import os
from datetime import datetime
import sqlite3
database_config = {
    'database': 'users.db'
}


def exit_app():
    exit()

def generate_text(user_name, user_gender, user_nationality, user_pass_num, user_housing, user_from_country, user_to_country):
    text = f"\nName: {user_name}\nGender: {user_gender}\nCountry: {user_nationality}\nPassport_num: {user_pass_num}\nHousing option: {user_housing}\nDate from: {user_from_country}\nDate to: {user_to_country}"
    return text

def generate_csv(list):
    header = ["id", "Name", "Gender", "Country", "Pass_Num", "Housing", "Date_from", "Date_to"]
    csv_values = [list]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"output_{timestamp}.csv"
    file_empty = not os.path.exists(filename) or os.path.getsize(filename) == 0

    with open(filename, "a", newline="") as file:
        csvwriter = csv.writer(file)
        
        # Write the header only if the file is empty
        if file_empty:
            csvwriter.writerow(header)

        csvwriter.writerows(csv_values)

def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, '%d/%m/%Y')
        return True
    except ValueError:
        return False
    
def append_values_to_database(values, database_config=database_config):
    try:
        connection = sqlite3.connect(database_config['database'])
        cursor = connection.cursor()


        query = """
            INSERT INTO users (name, gender, country, pass_num, housing, date_from, date_to)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(query, values)

        connection.commit()
        cursor.close()
        connection.close()

        print("Data appended to the database successfully.")

    except sqlite3.Error as err:
        print(f"Error: {err}")


def return_values_from_database(database_config=database_config):
    try:
        connection = sqlite3.connect(database_config['database'])
        cursor = connection.cursor()

        query = """
            SELECT * FROM users
        """
        cursor.execute(query)
        records = cursor.fetchall()
        cursor.close()
        connection.close()
        return records

    except sqlite3.Error as err:
        print(f"Error: {err}")



def delete_user_info(user_id, database_config=database_config):
    try:
        connection = sqlite3.connect(database_config['database'])
        cursor = connection.cursor()

        query = """
            DELETE FROM users
            WHERE user_id = ?
        """

        cursor.execute(query, (user_id,))

        connection.commit()
        cursor.close()
        connection.close()

        print(f"User with user_id {user_id} deleted successfully.")

    except sqlite3.Error as err:
        print(f"Error: {err}")

def update_user_info(user_id, new_values, database_config=database_config):
    try:
        
        connection = sqlite3.connect(database_config['database'])
        cursor = connection.cursor()

        query = """
            UPDATE users
            SET name = ?, gender = ?, country = ?, pass_num = ?, housing = ?, date_from = ?, date_to = ?
            WHERE user_id = ?
        """

        updated_values = new_values + (user_id,)

        cursor.execute(query, updated_values)

        connection.commit()
        cursor.close()
        connection.close()

        print(f"User with user_id {user_id} updated successfully.")

    except sqlite3.Error as err:
        print(f"Error: {err}")
