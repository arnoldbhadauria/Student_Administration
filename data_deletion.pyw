import tkinter as tk
from tkinter import messagebox
import mysql.connector as c

my_con = c.connect(host="localhost", user="root", passwd="####", database="student")
cursor = my_con.cursor()


def deleting_data():
    try:
        query = f"delete from student_info where id={id_txt.get()} and firstname='{firstname_txt.get()}';"
        cursor.execute(query)
        my_con.commit()
        messagebox.showinfo("Deleted", "Record has been 'deleted' from the database.")
    except my_con.connect as e:
        messagebox.showerror("Error", "Please fill the details properly.")
        clear_form()


def clear_form():
    id_txt.delete(0, tk.END)
    firstname_txt.delete(0, tk.END)


def cancel_func():
    exit()


window = tk.Tk()
window.title("Deletion")
window.geometry("400x200")
window.resizable(False, False)

window_font = "SF Pro"
window_fontSize = 10
x_axis = 30
y_axis = 30

instruction = tk.Label(window, text="Please enter info given below:", font=(window_font, window_fontSize))
instruction.place(x=x_axis, y=y_axis)

ID_lb = tk.Label(window, text="ID", width=10, font=(window_font, window_fontSize))
ID_lb.place(x=x_axis, y=y_axis + 40)

firstname_lb = tk.Label(window, width=10, text="Firstname", font=(window_font, window_fontSize), justify="center",
                        anchor="center")
firstname_lb.place(x=x_axis, y=y_axis + 80)

id_txt = tk.Entry(window, width=20, font=(window_font, window_fontSize))
id_txt.place(x=x_axis + 100, y=y_axis + 40)

firstname_txt = tk.Entry(window, width=20, font=(window_font, window_fontSize))
firstname_txt.place(x=x_axis + 100, y=y_axis + 80)

delete_btn = tk.Button(window, text="Delete", width=6, font=(window_font, window_fontSize), command=deleting_data)
delete_btn.place(x=x_axis + 280, y=y_axis)

clear_btn = tk.Button(window, text="Clear", width=6, font=(window_font, window_fontSize), command=clear_form)
clear_btn.place(x=x_axis + 280, y=y_axis + 40)

cancel_btn = tk.Button(window, text="Cancel", width=6, font=(window_font, window_fontSize), command=cancel_func)
cancel_btn.place(x=x_axis + 280, y=y_axis + 80)

window.mainloop()

