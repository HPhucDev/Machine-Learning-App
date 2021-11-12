import webbrowser
import re
import sys
import os
import tksheet
import tkinter as tk
from pathlib import Path
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import date

# Path to asset files for this GUI window.
ASSETS_PATH = Path(__file__).resolve().parent / "assets"

window = tk.Tk()
logo = tk.PhotoImage(file=ASSETS_PATH / "iconbitmap.gif")
window.call('wm', 'iconphoto', window._w, logo)
window.title("List Staff and Statistical")
window.geometry("1260x650")
window.configure(bg="#3A7FF6")

tabControl = ttk.Notebook(window)  # create tab

""" connect database :
import sqlite3
def connect():
    con1 = sqlite3.connect("<path/database_name>")
    cur1 = con1.cursor()
    cur1.execute("CREATE TABLE IF NOT EXISTS table1(id INTEGER PRIMARY KEY, First TEXT, Surname TEXT)")
    con1.commit()
    con1.close()
def View():
    con1 = sqlite3.connect("<path/database_name>")
    cur1 = con1.cursor()
    cur1.execute("SELECT * FROM <table_name>")
    rows = cur1.fetchall()    
    for row in rows:
        print(row) 
        tree.insert("", tk.END, values=row)        
    con1.close()
# connect to the database
connect() 
"""
# Tab List Staff Open
listStaffTab = ttk.Frame(tabControl)
tabControl.add(listStaffTab, text='List Staff')
tabControl.pack(expand=1, fill="both")

# Create Data Gridview Open
tree = ttk.Treeview(listStaffTab, column=(
    "c1", "c2", "c3", "c4", "c5", "c6"), show='headings')

tree.column("#1", anchor=tk.CENTER)
tree.heading("#1", text="Name")

tree.column("#2", anchor=tk.CENTER)
tree.heading("#2", text="Date of birth")

tree.column("#3", anchor=tk.CENTER)
tree.heading("#3", text="Address")

tree.column("#4", anchor=tk.CENTER)
tree.heading("#4", text="Salary")

tree.column("#5", anchor=tk.CENTER)
tree.heading("#5", text="Phone")

tree.column("#6", anchor=tk.CENTER)
tree.heading("#6", text="Email")

tree.pack()
# Create Data Gridview Close
# Create Buttons Open
save_btn_img = tk.PhotoImage(file=ASSETS_PATH / "btn_add.png")
save_btn = tk.Button(listStaffTab,
                     image=save_btn_img, borderwidth=10, highlightthickness=0, relief="flat")
save_btn.place(x=260, y=440, width=195, height=73)

refesh_btn_img = tk.PhotoImage(file=ASSETS_PATH / "btn_refesh.png")
refesh_btn = tk.Button(listStaffTab,
                       image=refesh_btn_img, borderwidth=10, highlightthickness=0, relief="flat")
refesh_btn.place(x=260+165, y=440, width=195, height=73)

remove_btn_img = tk.PhotoImage(file=ASSETS_PATH / "btn_remove.png")
remove_btn = tk.Button(listStaffTab,
                       image=remove_btn_img, borderwidth=10, highlightthickness=0, relief="flat")
remove_btn.place(x=260+165*2, y=440, width=195, height=73)

update_btn_img = tk.PhotoImage(file=ASSETS_PATH / "btn_update.png")
update_btn = tk.Button(listStaffTab,
                       image=update_btn_img, borderwidth=10, highlightthickness=0, relief="flat")
update_btn.place(x=260+165*3, y=440, width=195, height=73)
# Create Buttons Close
# Tab List Staff Close


# Tab Statistical Open
statisticalTab = ttk.Frame(tabControl)
tabControl.add(statisticalTab, text='Statistical')
tabControl.pack(expand=1, fill="both")

ttk.Label(statisticalTab,
          text="From                                                 to").grid(column=0,
                                                                               row=0,
                                                                               padx=30,
                                                                               pady=30)
total_label = ttk.Label(statisticalTab,
                        text="Total: ")
total_label.place(x=30, y=70)

carout_label = ttk.Label(statisticalTab,
                         text="Number of cars come out: ")
carout_label.place(x=30, y=110)

carin_label = ttk.Label(statisticalTab,
                        text="Number of cars available: ")
carin_label.place(x=30, y=150)


cal = DateEntry(statisticalTab, selectmode='day')
cal.grid(row=0, column=0, padx=15)
cal = DateEntry(statisticalTab, selectmode='day')
cal.grid(row=0, column=2, padx=15)

# Tab Statistical Close


window.resizable(False, False)
window.mainloop()
