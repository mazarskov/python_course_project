#used for clean project back-end code
import csv
import os
from datetime import datetime

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


def is_valid_date(date_string):
    try:
        # Attempt to parse the input string as a date in the DD/MM/YYYY format
        datetime.strptime(date_string, '%d/%m/%Y')
        return True
    except ValueError:
        # If parsing fails, the input is not in the correct format
        return False