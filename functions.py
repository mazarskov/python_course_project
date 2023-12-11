#used for clean project back-end code
import csv
import os

def exit_app():
    exit()

def generate_text(user_name, user_gender, user_nationality, user_pass_num, user_housing, user_from_country, user_to_country):
    text = f"\nName: {user_name}\nGender: {user_gender}\nNationality: {user_nationality}\nPassport_num: {user_pass_num}\nHousing option: {user_housing}\nFlying from: {user_from_country}\nFlying to: {user_to_country}"
    return text

def generate_csv(name, gender, nationality, pass_num, housing, from_country, to_country):
    header = ["Name", "Gender", "Nationality", "Pass_Num", "Housing", "Flying_from", "Flying_to"]
    csv_values = [[name, gender, nationality, pass_num, housing, from_country, to_country]]
    filename = "test_output.csv"
    file_empty = not os.path.exists(filename) or not os.path.getsize(filename)
    print(file_empty)
    with open(filename, "a", newline="") as file:
        csvwriter = csv.writer(file)
        if file_empty:
            csvwriter.writerow(header)
        csvwriter.writerows(csv_values)