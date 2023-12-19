#used for clean project front-end code

import customtkinter as ctk
from functions import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk, filedialog

def get_and_validate_user_input():
    user_pass_num = pass_input_field.get()
    user_name = name_input_field.get()
    user_country = country_input_field.get()
    user_gender = gender_var.get()
    user_housing = housing_option.get()
    user_from_date = from_date_input_field.get()
    user_to_date = to_date_input_field.get()
    valid_date_from = is_valid_date(user_from_date)
    valid_date_to = is_valid_date(user_to_date)

    if not valid_date_from:
        user_from_date = "Not right date format, must be DD/MM/YYYY"
    if not valid_date_to:
        user_to_date = "Not right date format, must be DD/MM/YYYY"

    return user_name, user_gender, user_country, user_pass_num, user_housing, user_from_date, user_to_date, valid_date_from, valid_date_to

def print_all():
    user_name, user_gender, user_country, user_pass_num, user_housing, user_from_date, user_to_date, valid_date_from, valid_date_to = get_and_validate_user_input()
    text = generate_text(user_name, user_gender, user_country, user_pass_num, user_housing, user_from_date, user_to_date)
    text2 = return_values_from_database()
    formatted_text = format_records(text2)
    #display_box.insert("0.0", "\n")
    #display_box.insert("0.0", formatted_text)
    lines = formatted_text.split('----------------')
    # Add each line as a separate item
    for line in lines:
        listbox.insert(tk.END, line)


def export_csv():
    user_name, user_gender, user_country, user_pass_num, user_housing, user_from_date, user_to_date, valid_date_from, valid_date_to = get_and_validate_user_input()
    if not valid_date_from or not valid_date_to:
        messagebox.showinfo("CSV export failed", "CSV export failed because date was not DD/MM/YYYY")
    else:
        generate_csv(user_name, user_gender, user_country, user_pass_num, user_housing, user_from_date, user_to_date)

def add_to_database():
    user_name, user_gender, user_country, user_pass_num, user_housing, user_from_date, user_to_date, valid_date_from, valid_date_to = get_and_validate_user_input()
    if not valid_date_from or not valid_date_to:
        messagebox.showinfo("SQL add failed", "SQL add failed because date was not DD/MM/YYYY")
    else:
        converted_from_date = datetime.strptime(user_from_date, '%d/%m/%Y').strftime('%Y-%m-%d')
        converted_to_date = datetime.strptime(user_to_date, '%d/%m/%Y').strftime('%Y-%m-%d')
        values = [user_name, user_gender, user_country, user_pass_num, user_housing, converted_from_date, converted_to_date]
        append_values_to_database(values)

    
def update_housing_options(*args):
    selected_gender = gender_var.get()

    new_values = []
    if selected_gender == "Male":
        new_values = ["Male_dorm"]
    elif selected_gender == "Female":
        new_values = ["Female_dorm"]
    else:
        new_values = ["Male_dorm", "Female_dorm"]

    # Destroy the existing housing_option and create a new one with updated values
    housing_option.destroy()
    create_housing_option(new_values)

def create_housing_option(values):
    global housing_option
    housing_option = ctk.CTkOptionMenu(frame, values=values, width=300)
    housing_option.place(relx=0.2, rely=0.8, anchor=ctk.W)


ctk.set_appearance_mode("light")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
app = ctk.CTk()  # create CTk window like you do with the Tk window
app.title("Hotel Booking Management System (Early build)")
app.geometry("1000x800")
gender_var = ctk.StringVar()


frame = ctk.CTkFrame(app, width=950, height=200, corner_radius=5)
frame.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)

menu_bar = tk.Menu(app)
app.config(menu=menu_bar)

developers_menu = tk.Menu(menu_bar, tearoff=0)
developers_menu.add_command(label="Show developer info", command=lambda: messagebox.showinfo("Developers", "Maksim"))

menu_bar.add_cascade(label="Developers", menu=developers_menu)
exit_button = ctk.CTkButton(app, text="Exit", command=exit_app, width=200)
exit_button.place(relx=0.87, rely=0.9, anchor=ctk.CENTER) 

name_input_field = ctk.CTkEntry(frame, placeholder_text="Type name here", width=300)
name_input_field.place(relx = 0.13, rely = 0.2, anchor=ctk.W)
name_label = ctk.CTkLabel(frame, text="Name", fg_color="transparent", font=('Arial', 15))
name_label.place(relx = 0.05, rely = 0.2, anchor=ctk.W)

country_input_field = ctk.CTkEntry(frame, placeholder_text="Type country here", width=300)
country_input_field.place(relx = 0.57, rely = 0.2, anchor=ctk.W)
country_label = ctk.CTkLabel(frame, text="Country", fg_color="transparent", font=('Arial', 15))
country_label.place(relx = 0.5, rely = 0.2, anchor=ctk.W)

pass_input_field = ctk.CTkEntry(frame, placeholder_text="Type passport number here", width=300)
pass_input_field.place(relx = 0.13, rely = 0.4, anchor=ctk.W)
pass_label = ctk.CTkLabel(frame, text="Passport", fg_color="transparent", font=('Arial', 15))
pass_label.place(relx = 0.05, rely = 0.4, anchor=ctk.W)

gender_label = ctk.CTkLabel(frame, text="Gender", fg_color="transparent", font=('Arial', 15))
gender_label.place(relx = 0.5, rely = 0.4, anchor=ctk.W)
male = ctk.CTkRadioButton(frame, text="Male", variable=gender_var, value="Male")
male.place(relx = 0.6, rely = 0.4, anchor=ctk.W)
female = ctk.CTkRadioButton(frame, text="Female", variable=gender_var, value="Female")
female.place(relx = 0.7, rely = 0.4, anchor=ctk.W)
no_gender = ctk.CTkRadioButton(frame, text="Prefer not to say", variable=gender_var, value="NaN")
no_gender.place(relx = 0.8, rely = 0.4, anchor=ctk.W)

from_label= ctk.CTkLabel(frame, text="From", fg_color="transparent", font=('Arial', 15))
from_label.place(relx = 0.05, rely = 0.6, anchor=ctk.W)
from_date_input_field = ctk.CTkEntry(frame, placeholder_text="Type from date here", width=300)
from_date_input_field.place(relx = 0.13, rely = 0.6, anchor=ctk.W)
to_label = ctk.CTkLabel(frame, text="to", fg_color="transparent", font=('Arial', 15))
to_label.place(relx = 0.452, rely = 0.6, anchor=ctk.W)
to_date_input_field = ctk.CTkEntry(frame, placeholder_text="Type to date here", width=300)
to_date_input_field.place(relx = 0.47, rely = 0.6, anchor=ctk.W)

housing_option_label = ctk.CTkLabel(frame, text="Accomodation type", fg_color="transparent", font=('Arial', 15))
housing_option_label.place(relx = 0.05, rely = 0.8, anchor=ctk.W)
housing_option = ctk.CTkOptionMenu(frame, values=["Female dorm", "Male dorm"], width=300)
housing_option.place(relx = 0.2, rely = 0.8, anchor=ctk.W)


button_data = [
    {"parent": app, "text": "Update entry", "command": print_all, "relx": 0.8, "rely": 0.4},
    {"parent": app, "text": "Search entry", "command": print_all, "relx": 0.8, "rely": 0.45},
    {"parent": app, "text": "View all entries", "command": print_all, "relx": 0.8, "rely": 0.5},
    {"parent": app, "text": "Delete selected entry", "command": print_all, "relx": 0.8, "rely": 0.55},
    #{"parent": frame, "text": "Export to csv", "command": export_csv, "relx": 0.55, "rely": 0.8}, 
    {"parent": frame, "text": "Book Now", "command": add_to_database, "relx": 0.8, "rely": 0.8}
]

for data in button_data:
    button = ctk.CTkButton(data["parent"], text=data["text"], command=data["command"])
    button.place(relx=data["relx"], rely=data["rely"], anchor=ctk.W)




#display_box = ctk.CTkTextbox(app, width=500, height=300)
#display_box.place(relx = 0.025, rely = 0.55, anchor=ctk.W)

listbox = tk.Listbox(app, width=120, height=20)
listbox.place(relx = 0.005, rely = 0.55, anchor=ctk.W)

gender_var.trace_add('write', update_housing_options)
app.resizable(False, False)
app.mainloop() #line that MUST be at the end of the code