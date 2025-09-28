import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector as c

my_con = c.connect(host="localhost", user="root", passwd="arnold999", database="student")
cursor = my_con.cursor()


def deleting_data():
    try:
        if select_field.get() == "ID":
            query = f"update student_info set {select_field.get()} = {int(new_val_txt.get())} where id={int(id_txt.get())};"
            cursor.execute(query)
            my_con.commit()
            messagebox.showinfo("Updated", "Record has been updated successfully.")
        elif select_field.get() == "Age":
            query = f"update student_info set {select_field.get()} = {int(new_val_txt.get())} where id={int(id_txt.get())};"
            cursor.execute(query)
            my_con.commit()
            messagebox.showinfo("Updated", "Record has been updated successfully.")
        else:
            query = f"update student_info set {select_field.get()} = '{new_val_txt.get()}' where id={int(id_txt.get())};"
            cursor.execute(query)
            my_con.commit()
            messagebox.showinfo("Updated", "Record has been updated successfully.")
    except my_con.connect as e:
        messagebox.showerror("Error", f"Please fill the details properly :: {e}")
        clear_form()


def clear_form():
    select_field.set("Select column..")
    new_val_txt.delete(0, tk.END)


def cancel_func():
    exit()


window = tk.Tk()
window.title("Record Update")
window.geometry("400x200")
window.resizable(False, False)

window_font = "SF Pro"
window_fontSize = 10
x_axis = 30
y_axis = 30

instruction = tk.Label(window, text="Please enter info given below:", font=(window_font, window_fontSize))
instruction.place(x=x_axis, y=y_axis)

id_lb = tk.Label(window, width=10, text="ID", font=(window_font, window_fontSize))
id_lb.place(x=x_axis, y=y_axis + 40)

select_lb = tk.Label(window, text="Select field:", width=10, font=(window_font, window_fontSize))
select_lb.place(x=x_axis, y=y_axis + 80)

new_val_lb = tk.Label(window, width=10, text="New value", font=(window_font, window_fontSize))
new_val_lb.place(x=x_axis, y=y_axis + 120)

id_txt = tk.Entry(window, width=23, font=(window_font, window_fontSize))
id_txt.place(x=x_axis + 100, y=y_axis + 40)

field_options = ["ID", "Firstname", "Lastname", "Age", "Gender", "Phone", "Address", "Email", "Class"]
select_field = ttk.Combobox(window, width=20, font=(window_font, window_fontSize), values=field_options,
                            state="readonly")
select_field.set("Select column..")
select_field.place(x=x_axis + 100, y=y_axis + 80)

new_val_txt = tk.Entry(window, width=23, font=(window_font, window_fontSize))
new_val_txt.place(x=x_axis + 100, y=y_axis + 120)

update_btn = tk.Button(window, text="Update", width=6, font=(window_font, window_fontSize), command=deleting_data)
update_btn.place(x=x_axis + 280, y=y_axis + 40)

clear_btn = tk.Button(window, text="Clear", width=6, font=(window_font, window_fontSize), command=clear_form)
clear_btn.place(x=x_axis + 280, y=y_axis + 80)

cancel_btn = tk.Button(window, text="Cancel", width=6, font=(window_font, window_fontSize), command=cancel_func)
cancel_btn.place(x=x_axis + 280, y=y_axis + 120)

window.mainloop()
