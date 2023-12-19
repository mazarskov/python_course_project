#used for clean project front-end code

import customtkinter as ctk
from functions import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

chosen_id = None
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
    if user_pass_num == "":
        user_pass_num = None
    if user_name == "":
        user_name = None
    if user_country == "":
        user_country = None
    return user_name, user_gender, user_country, user_pass_num, user_housing, user_from_date, user_to_date, valid_date_from, valid_date_to


def print_all():
    user_name, user_gender, user_country, user_pass_num, user_housing, user_from_date, user_to_date, valid_date_from, valid_date_to = get_and_validate_user_input()
    text = generate_text(user_name, user_gender, user_country, user_pass_num, user_housing, user_from_date, user_to_date)
    text2 = return_values_from_database()
    listbox.delete(0, tk.END)
    for list in text2:
        listbox.insert(tk.END, list)
    

def export_csv():
    list_of_users = []
    list_of_users = return_values_from_database()
    if list_of_users == []:
        messagebox.showinfo("Database empty", "Database empty, nothing to export")
    else:
        for list in list_of_users:
            generate_csv(list)
        messagebox.showinfo("Success", "CSV file successfully generated")


def add_to_database():
    user_name, user_gender, user_country, user_pass_num, user_housing, user_from_date, user_to_date, valid_date_from, valid_date_to = get_and_validate_user_input()
    if not valid_date_from or not valid_date_to:
        messagebox.showinfo("SQL add failed", "SQL add failed because date was not DD/MM/YYYY")
    else:
        values = [user_name, user_gender, user_country, user_pass_num, user_housing, user_from_date, user_to_date]
        append_values_to_database(values)
        messagebox.showinfo("Success", "Information successfully added to database")
        refresh_entries_list()


def update_housing_options(*args):
    selected_gender = gender_var.get()
    new_values = []
    if selected_gender == "Male":
        new_values = ["Male_dorm"]
    elif selected_gender == "Female":
        new_values = ["Female_dorm"]
    else:
        new_values = ["Male_dorm", "Female_dorm"]
    housing_option.destroy()
    create_housing_option(new_values)


def create_housing_option(values):
    global housing_option
    housing_option = ctk.CTkOptionMenu(frame, values=values, width=300)
    housing_option.place(relx=0.2, rely=0.8, anchor=ctk.W)


def update_entry():
    user_name, user_gender, user_country, user_pass_num, user_housing, user_from_date, user_to_date, valid_date_from, valid_date_to = get_and_validate_user_input()
    user_id = chosen_id
    if user_id == None:
        messagebox.showinfo("Update failed", "Update failed because no entry was selected")
    elif not valid_date_from or not valid_date_to:
        messagebox.showinfo("Update failed", "Update failed because date was not DD/MM/YYYY")
    else:
        new_values = (user_name, user_gender, user_country, user_pass_num, user_housing, user_from_date, user_to_date)
        update_user_info(user_id, new_values)
        refresh_entries_list()
        messagebox.showinfo("Success", "Information successfully updated")


def delete_entry():
    user_id = chosen_id
    if user_id:
        delete_user_info(int(user_id))
        refresh_entries_list()
    else:
        messagebox.showinfo("Delete failed", "Delete failed because no entry was selected")


def refresh_entries_list():
    listbox.delete(0, tk.END)
    entries = return_values_from_database()
    listbox.delete(0, tk.END)
    for list in entries:
        listbox.insert(tk.END, list)


def ouput_filtered_list():
    listbox.delete(0, tk.END)
    entries = search_entries()
    if entries == None:
        messagebox.showinfo("Search failed", "Search failed because no entries were found")
    else:
        listbox.delete(0, tk.END)
        for list in entries:
            listbox.insert(tk.END, list)


def clear_fields():
    global chosen_id
    to_date_input_field.delete(0, tk.END)
    from_date_input_field.delete(0, tk.END)
    pass_input_field.delete(0, tk.END)
    country_input_field.delete(0, tk.END)
    name_input_field.delete(0, tk.END)
    gender_var.set("NaN")
    chosen_id = None


def search_entries():
    user_name, user_gender, user_country, user_pass_num, user_housing, user_from_date, user_to_date, valid_date_from, valid_date_to = get_and_validate_user_input()
    condition = []
    if user_name:
        condition.append(f"name = '{user_name}'")
    #if user_gender:
        #condition.append(f"gender = '{user_gender}'") ----------------- This is disabled due to how the functionality of search is built
    if user_country:
        condition.append(f"country = '{user_country}'")
    if user_pass_num:
        condition.append(f"pass_num = '{user_pass_num}'")
    #if user_housing:
        #condition.append(f"housing = '{user_housing}'") ----------------- This is disabled due to how the functionality of search is built
    if valid_date_from:
        condition.append(f"date_from = '{user_from_date}'")
    if valid_date_to:
        condition.append(f"date_to = '{user_to_date}'")
    query = "SELECT * FROM users"
    if condition:
        query += " WHERE " + " AND ".join(condition)
        connection = sqlite3.connect(database_config['database'])
        cursor = connection.cursor()
        query = query
        cursor.execute(query)
        records = cursor.fetchall()
        connection.commit()
        cursor.close()
        connection.close()
        return records

def on_select(event):
    if event.widget.curselection():
        selected_item = event.widget.get(event.widget.curselection())
        print(f"You selected: {selected_item}")
        selected_id, name, gender, country, pass_num, housing, date_from, date_to = selected_item
        global chosen_id
        chosen_id = selected_id
        from_date_input_field.delete(0, tk.END)
        from_date_input_field.insert(0, date_from)
        to_date_input_field.delete(0, tk.END)
        to_date_input_field.insert(0, date_to)
        pass_input_field.delete(0, tk.END)
        pass_input_field.insert(0, pass_num)
        country_input_field.delete(0, tk.END)
        country_input_field.insert(0, country)
        name_input_field.delete(0, tk.END)
        name_input_field.insert(0, name)
        if gender == "Male":
            gender_var.set("Male")
        elif gender == "Female":
            gender_var.set("Female")
        elif gender_var == "Prefer not to say":
            gender_var.set("NaN")


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
developers_menu.add_command(label="Show developer info", command=lambda: messagebox.showinfo("Developers", "Maksim Azarskov and Amberleigh Wankel"))

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Export to .CSV", command=export_csv)

menu_bar.add_cascade(label="File", menu=file_menu)
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
housing_option = ctk.CTkOptionMenu(frame, values=["Female_dorm", "Male_dorm"], width=300)
housing_option.place(relx = 0.2, rely = 0.8, anchor=ctk.W)


button_data = [
    {"parent": app, "text": "Update entry", "command": update_entry, "relx": 0.8, "rely": 0.4},
    {"parent": app, "text": "Search entry", "command": ouput_filtered_list, "relx": 0.8, "rely": 0.45},
    {"parent": app, "text": "View all entries", "command": print_all, "relx": 0.8, "rely": 0.5},
    {"parent": app, "text": "Delete selected entry", "command": delete_entry, "relx": 0.8, "rely": 0.55},
    {"parent": frame, "text": "Book Now", "command": add_to_database, "relx": 0.8, "rely": 0.8},
    {"parent": app, "text": "Clear all fields", "command": clear_fields, "relx": 0.8, "rely": 0.7}
]

for data in button_data:
    button = ctk.CTkButton(data["parent"], text=data["text"], command=data["command"])
    button.place(relx=data["relx"], rely=data["rely"], anchor=ctk.W)


style = ttk.Style()
style.configure("TListbox", background="white", foreground="black")
listbox = tk.Listbox(app, selectbackground="lightblue", selectforeground="black", bg="white", fg="black", width=60, height=20)
listbox.pack()
listbox.place(relx = 0.005, rely = 0.55, anchor=ctk.W)
listbox.bind('<<ListboxSelect>>', on_select)

gender_var.trace_add('write', update_housing_options)
app.resizable(False, False)
app.mainloop() #line that MUST be at the end of the code