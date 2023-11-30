#used for clean project front-end code

import customtkinter as ctk
from functions import *


ctk.set_appearance_mode("light")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
app = ctk.CTk()  # create CTk window like you do with the Tk window
app.title("Hotel Booking Management System (Early build)")
app.geometry("1000x800")
gender_var = ctk.StringVar()
user_name = "Not provided"
user_nationality = "Not provided"
user_gender = "Not provided"
user_pass_num = 0
user_hosuing = None
user_from_country = "Not provided"
user_to_country = "Not provided"

frame = ctk.CTkFrame(app, width=950, height=200, corner_radius=5)
frame.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)

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

from_label= ctk.CTkLabel(frame, text="Flying from", fg_color="transparent", font=('Arial', 15))
from_label.place(relx = 0.05, rely = 0.6, anchor=ctk.W)
from_country_input_field = ctk.CTkEntry(frame, placeholder_text="Type country here", width=300)
from_country_input_field.place(relx = 0.13, rely = 0.6, anchor=ctk.W)
to_label = ctk.CTkLabel(frame, text="to", fg_color="transparent", font=('Arial', 15))
to_label.place(relx = 0.452, rely = 0.6, anchor=ctk.W)
to_country_input_field = ctk.CTkEntry(frame, placeholder_text="Type destination country here", width=300)
to_country_input_field.place(relx = 0.47, rely = 0.6, anchor=ctk.W)

housing_option_label = ctk.CTkLabel(frame, text="Accomodation type", fg_color="transparent", font=('Arial', 15))
housing_option_label.place(relx = 0.05, rely = 0.8, anchor=ctk.W)
housing_option = ctk.CTkOptionMenu(frame, values=["Bim", "Bam", "Bum"], width=300)
housing_option.place(relx = 0.2, rely = 0.8, anchor=ctk.W)

def print_all(): #this is for testing only, not to be used in final project
    user_pass_num = pass_input_field.get()
    user_name = name_input_field.get()
    user_nationality = country_input_field.get()
    user_gender = gender_var.get()
    user_housing = housing_option.get()
    user_from_country = from_country_input_field.get()
    user_to_country = to_country_input_field.get()
    text = f"Name: {user_name}\nGender: {user_gender}\nNationality: {user_nationality}\nPassport_num: {user_pass_num}\nHousing option: {user_housing}\nFlying from: {user_from_country}\nFlying to: {user_to_country}"
    display_box.delete("0.0", "500.0")
    display_box.insert("0.0", text)

random_ass_button = ctk.CTkButton(frame, text="Print everything to console", command=print_all)
random_ass_button.place(relx = 0.8, rely = 0.8, anchor=ctk.W)

display_box = ctk.CTkTextbox(app, width=500, height=300)
display_box.place(relx = 0.025, rely = 0.55, anchor=ctk.W)

app.resizable(False, False)
app.mainloop() #line that MUST be at the end of the code