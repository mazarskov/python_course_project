#used for clean project back-end code
import csv
import os
from datetime import datetime
import mysql.connector
from pprint import pprint
from pprint import pformat
import customtkinter as ctk
from tkinter import messagebox
database_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'python_course_pass',
    'database': 'users'
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
        formatted_text += f"\nName: {record['name']}"
        formatted_text += f"\nGender: {record['gender']}"
        formatted_text += f"\nCountry: {record['country']}"
        formatted_text += f"\nPassport Number: {record['pass_num']}"
        formatted_text += f"\nHousing: {record['housing']}"
        formatted_text += f"\nDate From: {record['date_from']}"
        formatted_text += f"\nDate To: {record['date_to']}"
        formatted_text += "----------------"
    return formatted_text

def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, '%d/%m/%Y')
        return True
    except ValueError:
        return False
    

def append_values_to_database(values, database_config=database_config):
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(**database_config)
        cursor = connection.cursor()

        # Insert data into the database
        query = """
            INSERT INTO users (name, gender, country, pass_num, housing, date_from, date_to)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, values)

        # Commit the changes and close the connection
        connection.commit()
        cursor.close()
        connection.close()

        print("Data appended to the database successfully.")
        messagebox.showinfo("Data added successfully", "Data added successfully")

    except mysql.connector.Error as err:
        print(f"Error: {err}")


def convert_to_mysql_date(date_str):
    # Convert 'DD/MM/YYYY' to 'YYYY-MM-DD'
    try:
        date_object = datetime.strptime(date_str, '%d/%m/%Y')
        return date_object.strftime('%Y-%m-%d')
    except ValueError:
        return None
    


def return_values_from_database(database_config=database_config):
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(**database_config)
        cursor = connection.cursor()

        # Get data from the database
        query = """
            SELECT * FROM users
        """
        cursor.execute(query)
        column_names = [i[0] for i in cursor.description]
        records = cursor.fetchall()

        # Format the data
        formatted_records = [dict(zip(column_names, record)) for record in records]

        cursor.close()
        connection.close()

        return formatted_records

    except mysql.connector.Error as err:
        print(f"Error: {err}")
