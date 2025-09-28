import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector as c
import os

my_con = c.connect(host="localhost", user="root", passwd="arnold999", database="student")
cursor = my_con.cursor()
field_values = []


def open_update_window():
    os.startfile("update_row.pyw")


def open_data_deletion_window():
    os.startfile("data_deletion.pyw")


def open_search_record_window():
    os.startfile("search_record.pyw")


def open_tabular_form_window():
    os.startfile("tabular_data_form.pyw")


def data_upload_into_sql():
    try:
        query = f"insert into student_info values ({int(id_txt.get())}, '{firstname_txt.get()}','{lastname_txt.get()}', {int(age_txt.get())}, '{gender_combobox.get()}', '{phone_txt.get()}', '{address_txt.get()}', '{email_txt.get()}', '{class_combobox.get()}');"
        cursor.execute(query)
        my_con.commit()
        print("Data upload completed.")
    except my_con.connector as e:
        print(f"There is a error occurred :: {e}")
        messagebox.showerror("Error",
                             "An error is occurred during uploading data. Looks like entered ID already exist.")


def clear_function():
    id_txt.delete(0, tk.END)
    firstname_txt.delete(0, tk.END)
    lastname_txt.delete(0, tk.END)
    age_txt.delete(0, tk.END)
    gender_combobox.set("Select Gender")
    phone_txt.delete(0, tk.END)
    address_txt.delete(0, tk.END)
    email_txt.delete(0, tk.END)
    class_combobox.set("Select Class")


def quiting_GUI():
    exit()


def checking_data_correctness():
    def is_not_numeric_string(variable):
        return not variable.isnumeric()

    if id_txt.get() == "" or firstname_txt.get() == "" or lastname_txt == "" or age_txt == "" or gender_combobox.get() == "" or phone_txt.get() == "" or address_txt.get() == "" or email_txt.get() == "" or class_combobox.get() == "":
        messagebox.showerror("Unfilled Input", "Please fill details properly. Entry can't be empty.")
    elif is_not_numeric_string(age_txt.get()):
        messagebox.showerror("Wrong Input", "Please enter 'Age' correctly. Age should be integer.")
    elif is_not_numeric_string(id_txt.get()):
        messagebox.showerror("Wrong Input", "Please enter 'ID' correctly. ID should be integer.")
    elif len(phone_txt.get()) != 10:
        messagebox.showerror("Wrong Input", "Please enter 'Phone' correctly. Phone number should be 10 digit long.")
    elif is_not_numeric_string(phone_txt.get()):
        messagebox.showerror("Wrong Input", "Please enter 'Phone' correctly. Phone number should be integer.")
    elif ".com" not in email_txt.get():
        messagebox.showerror("Wrong Input", "Please enter 'Email' correctly. Email is not valid.")

    else:
        print("All entries are correct.")
        data_upload_into_sql()
        messagebox.showinfo("Data upload", "Information successfully uploaded.")
        clear_function()


window = tk.Tk()
window.title("Administration")
window.geometry("650x650")
window.resizable(False, False)

window_font = "SF Pro"
window_fontSize = 10
x_axis = 50
y_axis = 100

# age_var = IntVar()
# phone_var = IntVar()

# Heading of the Application
heading = tk.Label(window, text="Student Administration", font=(window_font, 30))
heading.place(x=x_axis, y=y_axis - 75)

# Data entry tags
ID_lb = tk.Label(window, text="ID", width=10, font=(window_font, window_fontSize), justify="center", anchor="center")
ID_lb.place(x=x_axis, y=y_axis)

firstname_lb = tk.Label(window, width=10, text="Firstname", font=(window_font, window_fontSize), justify="center",
                        anchor="center")
firstname_lb.place(x=x_axis, y=y_axis + 50)

lastname_lb = tk.Label(window, width=10, text="Lastname", font=(window_font, window_fontSize), justify="center",
                       anchor="center")
lastname_lb.place(x=x_axis, y=y_axis + 100)

Age_lb = tk.Label(window, width=10, text="Age", font=(window_font, window_fontSize), justify="center", anchor="center")
Age_lb.place(x=x_axis, y=y_axis + 150)

Gender_lb = tk.Label(window, width=10, text="Gender", font=(window_font, window_fontSize), justify="center",
                     anchor="center")
Gender_lb.place(x=x_axis, y=y_axis + 200)

Phone_lb = tk.Label(window, width=10, text="Phone", font=(window_font, window_fontSize), justify="center",
                    anchor="center")
Phone_lb.place(x=x_axis, y=y_axis + 250)

address_lb = tk.Label(window, width=10, text="Address", font=(window_font, window_fontSize), justify="center",
                      anchor="center")
address_lb.place(x=x_axis, y=y_axis + 300)

email_lb = tk.Label(window, width=10, text="E-mail", font=(window_font, window_fontSize), justify="center",
                    anchor="center")
email_lb.place(x=x_axis, y=y_axis + 350)

class_lb = tk.Label(window, width=10, text="Class", font=(window_font, window_fontSize), justify="center",
                    anchor="center")
class_lb.place(x=x_axis, y=y_axis + 400)

# textbox for entry data
id_txt = tk.Entry(window, width=10, font=(window_font, window_fontSize))
id_txt.place(x=x_axis + 200, y=y_axis)

firstname_txt = tk.Entry(window, width=25, font=(window_font, window_fontSize))
firstname_txt.place(x=x_axis + 200, y=y_axis + 50)

lastname_txt = tk.Entry(window, width=25, font=(window_font, window_fontSize))
lastname_txt.place(x=x_axis + 200, y=y_axis + 100)

age_txt = tk.Entry(window, width=10, font=(window_font, window_fontSize))
age_txt.place(x=x_axis + 200, y=y_axis + 150)

# gender_txt = tk.Entry(window, width=10, font=(window_font, window_fontSize))
# gender_txt.place(x=x_axis+200, y=y_axis+200)
items = ["Male", "Female", "Unknown"]
gender_combobox = ttk.Combobox(window, values=items, state="readonly")
gender_combobox.set("Select Gender")
gender_combobox.place(x=x_axis + 200, y=y_axis + 200)

phone_txt = tk.Entry(window, width=20, font=(window_font, window_fontSize))
phone_txt.place(x=x_axis + 200, y=y_axis + 250)

address_txt = tk.Entry(window, width=30, font=(window_font, window_fontSize))
address_txt.place(x=x_axis + 200, y=y_axis + 300)

email_txt = tk.Entry(window, width=30, font=(window_font, window_fontSize))
email_txt.place(x=x_axis + 200, y=y_axis + 350)

classes = ["Nursery", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"]
class_combobox = ttk.Combobox(window, values=classes, state="readonly")
class_combobox.set("Select Class")
class_combobox.place(x=x_axis + 200, y=y_axis + 400)

# Buttons for GUI
btn_x = 500
btn_y = 100
submit_btn = tk.Button(window, text="Submit", height=3, width=10, font=(window_font, window_fontSize),
                       command=checking_data_correctness)
submit_btn.place(x=btn_x, y=btn_y)

clear_btn = tk.Button(window, text="Clear", height=3, width=10, font=(window_font, window_fontSize),
                      command=clear_function)
clear_btn.place(x=btn_x, y=btn_y + 100)

alter_btn = tk.Button(window, text="Update", height=3, width=10, font=(window_font, window_fontSize),
                      command=open_update_window)
alter_btn.place(x=btn_x, y=btn_y + 200)

del_btn = tk.Button(window, text="Delete", height=3, width=10, font=(window_font, window_fontSize),
                    command=open_data_deletion_window)
del_btn.place(x=btn_x, y=btn_y + 300)

exit_btn = tk.Button(window, text="Exit", height=3, width=10, font=(window_font, window_fontSize), command=quiting_GUI)
exit_btn.place(x=btn_x, y=btn_y + 400)

# special buttons
s_x = 50
s_y = 500

sub_heading = tk.Label(window, text="___________________________________________", font=(window_font, 12))
sub_heading.place(x=s_x, y=s_y + 30)

find_btn = tk.Button(window, text="Find record", height=2, width=10, font=(window_font, window_fontSize), command= open_search_record_window)
find_btn.place(x=s_x, y=s_y + 70)

view_btn = tk.Button(window, text="View records", height=2, width=10, font=(window_font, window_fontSize), command=open_tabular_form_window)
view_btn.place(x=s_x + 100, y=s_y + 70)

window.mainloop()
