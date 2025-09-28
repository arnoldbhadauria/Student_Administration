import tkinter as tk
from tkinter import ttk
import mysql.connector as c

my_con = c.connect(host="localhost", user="root", passwd="arnold999", database="student")
cursor = my_con.cursor()

root = tk.Tk()
root.title("Student Information")
root.geometry("1100x700")

# Create the treeview widget with 'headings' option to remove row numbers
table = ttk.Treeview(root, show='headings')

# Add columns to the treeview
table["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9")

# Set column headings
table.heading("1", text="ID")
table.heading("2", text="Firstname")
table.heading("3", text="Lastname")
table.heading("4", text="Age")
table.heading("5", text="Gender")
table.heading("6", text="Phone")
table.heading("7", text="Address")
table.heading("8", text="Email")
table.heading("9", text="Class")

table.column("1", width=70)
table.column("2", width=150)
table.column("3", width=150)
table.column("4", width=70)
table.column("5", width=80)
table.column("6", width=100)
table.column("7", width=150)
table.column("8", width=250)
table.column("9", width=50)

table_style = ttk.Style()
table_style.configure("Custom.Treeview", highlightthickness=1, bd=0)

# Insert data into the table (sample data for demonstration purposes)
query = "select * from student_info;"
cursor.execute(query)
data = cursor.fetchall()
for value in data:
    table.insert("", "end", values=(value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7], value[8]))

# Pack the treeview to display it in the window
table.pack()

root.mainloop()
