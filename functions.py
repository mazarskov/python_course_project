#used for clean project back-end code
import csv
import os
from datetime import datetime
from pprint import pprint
from pprint import pformat
import customtkinter as ctk
from tkinter import messagebox
import sqlite3
database_config = {
    'database': 'users.db'
}


def exit_app():
    exit()

def generate_text(user_name, user_gender, user_nationality, user_pass_num, user_housing, user_from_country, user_to_country):
    text = f"\nName: {user_name}\nGender: {user_gender}\nCountry: {user_nationality}\nPassport_num: {user_pass_num}\nHousing option: {user_housing}\nDate from: {user_from_country}\nDate to: {user_to_country}"
    return text

def generate_csv(name, gender, nationality, pass_num, housing, from_country, to_country):
    header = ["Name", "Gender", "Country", "Pass_Num", "Housing", "Date_from", "Date_to"]
    csv_values = [[name, gender, nationality, pass_num, housing, from_country, to_country]]
    filename = "test_output.csv"
    file_empty = not os.path.exists(filename) or not os.path.getsize(filename)
    print(file_empty)
    with open(filename, "a", newline="") as file:
        csvwriter = csv.writer(file)
        if file_empty:
            csvwriter.writerow(header)
        csvwriter.writerows(csv_values)


def format_records(records):
    formatted_text = ""
    for record in records:
        if isinstance(record, dict):
            formatted_text += f"\nName: {record.get('name', 'N/A')}"
            formatted_text += f"\nGender: {record.get('gender', 'N/A')}"
            formatted_text += f"\nCountry: {record.get('country', 'N/A')}"
            formatted_text += f"\nPassport Number: {record.get('pass_num', 'N/A')}"
            formatted_text += f"\nHousing: {record.get('housing', 'N/A')}"
            formatted_text += f"\nDate From: {record.get('date_from', 'N/A')}"
            formatted_text += f"\nDate To: {record.get('date_to', 'N/A')}"
            formatted_text += "----------------"
        else:
            formatted_text += f"\nUnexpected record format: {record}"
    return formatted_text



def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, '%d/%m/%Y')
        return True
    except ValueError:
        return False
    

def append_values_to_database(values, database_config=database_config):
    try:
        # Connect to the SQLite database
        connection = sqlite3.connect(database_config['database'])
        cursor = connection.cursor()

        # Insert data into the database
        query = """
            INSERT INTO users (name, gender, country, pass_num, housing, date_from, date_to)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(query, values)

        # Commit the changes and close the connection
        connection.commit()
        cursor.close()
        connection.close()

        print("Data appended to the database successfully.")

    except sqlite3.Error as err:
        print(f"Error: {err}")

'''
def convert_to_mysql_date(date_str):
    # Convert 'DD/MM/YYYY' to 'YYYY-MM-DD'
    try:
        date_object = datetime.strptime(date_str, '%d/%m/%Y')
        return date_object.strftime('%Y-%m-%d')
    except ValueError:
        return None
'''


def return_values_from_database(database_config=database_config):
    try:
        # Connect to the SQLite database
        connection = sqlite3.connect(database_config['database'])
        cursor = connection.cursor()

        # Get data from the database
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
        # Connect to the SQLite database
        connection = sqlite3.connect(database_config['database'])
        cursor = connection.cursor()

        # Construct the DELETE query
        query = """
            DELETE FROM users
            WHERE user_id = ?
        """

        # Execute the query
        cursor.execute(query, (user_id,))

        # Commit the changes and close the connection
        connection.commit()
        cursor.close()
        connection.close()

        print(f"User with user_id {user_id} deleted successfully.")

    except sqlite3.Error as err:
        print(f"Error: {err}")