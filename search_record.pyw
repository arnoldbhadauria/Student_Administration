import tkinter as tk
# from tkinter import ttk, messagebox
import mysql.connector as c

my_con = c.connect(host="localhost", user="root", passwd="arnold999", database="student")
cursor = my_con.cursor()


def extracting_record_from_sql():
    query = f"select * from student_info where id = {id_txt.get()};"
    cursor.execute(query)

    data = cursor.fetchall()
    firstname_txt['text'] = f'{data[0][1]}'
    lastname_txt['text'] = f'{data[0][2]}'
    age_txt['text'] = f'{data[0][3]}'
    gender_txt['text'] = f'{data[0][4]}'
    phone_txt['text'] = f'{data[0][5]}'
    address_txt['text'] = f'{data[0][6]}'
    email_txt['text'] = f'{data[0][7]}'
    class_txt['text'] = f'{data[0][8]}'


def clear_function():
    firstname_txt['text'] = ''
    lastname_txt['text'] = ''
    age_txt['text'] = ''
    gender_txt['text'] = ''
    phone_txt['text'] = ''
    address_txt['text'] = ''
    email_txt['text'] = ''
    class_txt['text'] = ''


def quiting_GUI():
    exit()


window = tk.Tk()
window.title("Record Update")
window.geometry("650x600")
window.resizable(False, False)

window_font = "SF Pro"
window_fontSize = 10
x_axis = 50
y_axis = 100

# age_var = IntVar()
# phone_var = IntVar()

# Heading of the Application
heading = tk.Label(window, text="Search Record", font=(window_font, 20))
heading.place(x=x_axis, y=y_axis - 75)


# Data entry tags
ID_lb = tk.Label(window, text="Enter the ID:", width=10, font=(window_font, window_fontSize), justify="center", anchor="center")
ID_lb.place(x=x_axis, y=y_axis)

sub_heading = tk.Label(window, text="___________________________________________", font=(window_font, 12))
sub_heading.place(x=x_axis, y=y_axis + 18)

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

# information

id_txt = tk.Entry(window, width=20, font=(window_font, window_fontSize))
id_txt.place(x=x_axis + 200, y=y_axis)

firstname_txt = tk.Label(window, text="", font=(window_font, window_fontSize))
firstname_txt.place(x=x_axis + 200, y=y_axis + 50)

lastname_txt = tk.Label(window, text="", font=(window_font, window_fontSize))
lastname_txt.place(x=x_axis + 200, y=y_axis + 100)

age_txt = tk.Label(window, text="", font=(window_font, window_fontSize))
age_txt.place(x=x_axis + 200, y=y_axis + 150)

# gender_txt = tk.Label(window, width=10, font=(window_font, window_fontSize))
# gender_txt.place(x=x_axis+200, y=y_axis+200)
gender_txt = tk.Label(window, text="", font=(window_font, window_fontSize))
gender_txt.place(x=x_axis + 200, y=y_axis + 200)

phone_txt = tk.Label(window, text="", font=(window_font, window_fontSize))
phone_txt.place(x=x_axis + 200, y=y_axis + 250)

address_txt = tk.Label(window, text="", font=(window_font, window_fontSize))
address_txt.place(x=x_axis + 200, y=y_axis + 300)

email_txt = tk.Label(window, text="", font=(window_font, window_fontSize))
email_txt.place(x=x_axis + 200, y=y_axis + 350)

class_txt = tk.Label(window, text="", font=(window_font, window_fontSize))
class_txt.place(x=x_axis + 200, y=y_axis + 400)


# Buttons for GUI
btn_x = 500
btn_y = 100
search_btn = tk.Button(window, text="Search", height=3, width=10, font=(window_font, window_fontSize),
                       command=extracting_record_from_sql)
search_btn.place(x=btn_x, y=btn_y)

clear_btn = tk.Button(window, text="Clear", height=3, width=10, font=(window_font, window_fontSize),
                      command=clear_function)
clear_btn.place(x=btn_x, y=btn_y + 100)

exit_btn = tk.Button(window, text="Cancel", height=3, width=10, font=(window_font, window_fontSize), command=quiting_GUI)
exit_btn.place(x=btn_x, y=btn_y + 200)

window.mainloop()
