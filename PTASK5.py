
import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Establish database connection
con = mysql.connector.connect(host="localhost", user="root", password="root")
cur = con.cursor(buffered=True)

try:
    cur.execute("use bhavesh")
except mysql.connector.Error:
    cur.execute("create database bhavesh")
    cur.execute("use bhavesh")

try:
    cur.execute("desc contacts")
except mysql.connector.Error:
    cur.execute("Create table contacts(name varchar(20), number int primary key, email varchar(20), address varchar(50))")

def execute_query(query, commit=False):
    try:
        cur.execute(query)
        if commit:
            con.commit()
        return True
    except mysql.connector.Error as e:
        messagebox.showinfo("Error", f"Database error: {str(e)}")
        return False

def Add():
    query = f"INSERT INTO contacts(name, number, email, address) VALUES ('{E1.get()}','{E2.get()}','{E3.get()}','{E4.get()}')"
    if execute_query(query, commit=True):
        messagebox.showinfo("Insertion Details", "New Contact Details have been added successfully!")

def View():
    cur.execute("SELECT * FROM contacts")
    rows = cur.fetchall()

    # Prepare a string to display all records
    records_str = ""
    for i, row in enumerate(rows):
        records_str += f"Record {i + 1}:\n"
        records_str += f"Name: {row[0]}\n"
        records_str += f"Number: {row[1]}\n"
        records_str += f"Email: {row[2]}\n"
        records_str += f"Address: {row[3]}\n"
        records_str += "\n"

    # Display records in a messagebox
    messagebox.showinfo("View Contacts", records_str)

def Search():
    global search_window
    search_window = tk.Toplevel(win)
    search_window.title("Search Contact")
    search_window.geometry("300x100")

    L5 = tk.Label(search_window, text="Enter the Phone Number to SEARCH:")
    L5.grid(row=1, column=1)
    global E5
    E5 = tk.Entry(search_window)
    E5.grid(row=1, column=2)
    B6 = tk.Button(search_window, text="Search", command=Search1)
    B6.grid(row=2, column=1, columnspan=2)

def Search1():
    cur.execute(f"SELECT * FROM contacts WHERE number={E5.get()}")
    rows1 = cur.fetchall()

    records_str1 = ""
    for i, row in enumerate(rows1):
        records_str1 += f"Record {i + 1} Found :- \n"
        records_str1 += f"Name: {row[0]}\n"
        records_str1 += f"Number: {row[1]}\n"
        records_str1 += f"Email: {row[2]}\n"
        records_str1 += f"Address: {row[3]}\n"
        records_str1 += "\n"

    # Display records in a messagebox
    messagebox.showinfo("View Contacts", records_str1)
    search_window.destroy()

def Update():
    global update_window
    update_window = tk.Toplevel(win)
    update_window.title("Update Contact")
    update_window.geometry("400x150")

    L7 = tk.Label(update_window, text="Enter which Field Name that you want to Update:")
    L7.grid(row=1, column=1)
    global E7
    E7 = tk.Entry(update_window)
    E7.grid(row=1, column=2)
    B8 = tk.Button(update_window, text="Submit", command=Update1)
    B8.grid(row=2, column=1, columnspan=2)

def Update1():
    global comm, comm2, E8, E9, update_window
    comm = E7.get()
    comm2 = comm.lower()

    L8 = tk.Label(update_window, text="Enter the Phone Number to UPDATE Contact Details:")
    L8.grid(row=3, column=1)
    global E8
    E8 = tk.Entry(update_window)
    E8.grid(row=3, column=2)

    L9 = tk.Label(update_window, text="Enter the New Data for what you want to make CHANGES:")
    L9.grid(row=4, column=1)
    global E9
    E9 = tk.Entry(update_window)
    E9.grid(row=4, column=2)

    B9 = tk.Button(update_window, text="Submit", command=Update2)
    B9.grid(row=5, column=1, columnspan=2)

def Update2():
    global comm2, E8, E9, update_window
    if comm2 == "name":
        query = f"UPDATE contacts SET name='{E9.get()}' WHERE number='{E8.get()}'"
    elif comm2 == "email":
        query = f"UPDATE contacts SET email='{E9.get()}' WHERE number='{E8.get()}'"
    elif comm2 == "address":
        query = f"UPDATE contacts SET address='{E9.get()}' WHERE number='{E8.get()}'"
    
    if execute_query(query, commit=True):
        messagebox.showinfo("Update Details", f"{comm2.capitalize()} has been UPDATED!")

    update_window.destroy()

def Delete():
    global delete_window
    delete_window = tk.Toplevel(win)
    delete_window.title("Delete Contact")
    delete_window.geometry("300x100")

    L6 = tk.Label(delete_window, text="Enter the Phone Number to DELETE:")
    L6.grid(row=1, column=1)
    global E6
    E6 = tk.Entry(delete_window)
    E6.grid(row=1, column=2)
    B7 = tk.Button(delete_window, text="Submit", command=Delete1)
    B7.grid(row=2, column=1, columnspan=2)

def Delete1():
    query = f"DELETE FROM contacts WHERE number={E6.get()}"
    if execute_query(query, commit=True):
        messagebox.showinfo("View Contacts", f"{E6.get()} has been DELETED!")

    delete_window.destroy()

# Main window
win = tk.Tk()
win.geometry("600x400")
win.title("Contact Book")

L=tk.Label(win,text="CONTACT BOOK")
L1=tk.Label(win,text="Name :- ")
L2=tk.Label(win,text="Phone Number :- ")
L3=tk.Label(win,text="Email :- ")
L4=tk.Label(win,text="Address :- ")

L.grid(row=1,column=2)
L1.grid(row= 4, column=1)
L2.grid(row= 5, column=1)
L3.grid(row= 6, column=1)
L4.grid(row= 7, column=1)
E1=tk.Entry(win)
E2=tk.Entry(win)
E3=tk.Entry(win)
E4=tk.Entry(win)
E1.grid(row=4,column=3)
E2.grid(row=5,column=3)
E3.grid(row=6,column=3)
E4.grid(row=7,column=3)
B1=tk.Button(win,text="Add Contact",command=Add)
B2=tk.Button(win,text="View Contact",command=View)
B3=tk.Button(win,text="Search Contact",command=Search)
B4=tk.Button(win,text="Update Contact",command=Update)
B5=tk.Button(win,text="Delete Contact",command=Delete)
B1.grid(row=10,column=1)
B2.grid(row=10,column=3)
B3.grid(row=12,column=1)
B4.grid(row=12,column=3)
B5.grid(row=14,column=2)
win.configure(bg="lightblue")

win.mainloop()