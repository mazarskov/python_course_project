#used for clean project back-end code
import csv
import os
from datetime import datetime
import mysql.connector
database_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Maksim2010',
    'database': 'users'
}


def exit_app():
    exit()

def generate_text(user_name, user_gender, user_nationality, user_pass_num, user_housing, user_from_country, user_to_country):
    text = f"\nName: {user_name}\nGender: {user_gender}\nCountry: {user_nationality}\nPassport_num: {user_pass_num}\nHousing option: {user_housing}\nDate from: {type(user_from_country)}\nDate to: {user_to_country}"
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

    except mysql.connector.Error as err:
        print(f"Error: {err}")


def convert_to_mysql_date(date_str):
    # Convert 'DD/MM/YYYY' to 'YYYY-MM-DD'
    try:
        date_object = datetime.strptime(date_str, '%d/%m/%Y')
        return date_object.strftime('%Y-%m-%d')
    except ValueError:
        return None
    
def print_values_from_database(database_config=database_config):
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(**database_config)
        cursor = connection.cursor()

        # Get data from the database
        query = """
            SELECT * FROM users
        """
        cursor.execute(query)
        records = cursor.fetchall()
        for row in records:
            print(row)

        # Close the connection
        cursor.close()
        connection.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

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
        records = cursor.fetchall()
        cursor.close()
        connection.close()
        return records

        # Close the connection
        

    except mysql.connector.Error as err:
        print(f"Error: {err}")