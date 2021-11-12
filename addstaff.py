import webbrowser
import re
import sys
import os
import tkinter as tk
from pathlib import Path
from tkinter import *
from PIL import Image, ImageTk
from tkcalendar import Calendar
from tkcalendar import DateEntry
from datetime import date
# Path to asset files for this GUI window.
ASSETS_PATH = Path(__file__).resolve().parent / "assets"

window = tk.Tk()
logo = tk.PhotoImage(file=ASSETS_PATH / "iconbitmap.gif")
window.call('wm', 'iconphoto', window._w, logo)
window.title("Add Staff")
window.geometry("740x700")
window.configure(bg="#3A7FF6")

canvas = tk.Canvas(
    window, bg="#ffffff", height=760, width=760,
    bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

canvas.create_text(
    170.5, 38.0, text="Staff Infomations",
    fill="#000000", font=("Arial-BoldMT", int(38.0)))


text_box_bg = tk.PhotoImage(
    file=ASSETS_PATH / "TextBox_Bg.png")  # Textbox background

fullname_entry_img = canvas.create_image(
    180.0, 126.5, image=text_box_bg)  # background
fullname_entry = tk.Entry(bd=0, bg="#F6F7F9", highlightthickness=0)
fullname_entry.place(x=20.0, y=112, width=321.0, height=35)
fullname_entry.focus()
canvas.create_text(
    20.0, 106.0, text="Full name: ", fill="#515486",
    font=("Arial-BoldMT", int(13.0)), anchor="w")

date_entry_img = canvas.create_image(
    180.0+370, 130, image=text_box_bg)  # background
canvas.create_text(
    180.0+250, 110.0, text="Date of Birth:",
    fill="#000000", font=("Arial-BoldMT", int(13.0)))
cal = DateEntry(window, background='#ECECEC', selectmode='day')
cal.place(x=180.0+320, y=120)

address_entry_img = canvas.create_image(
    180.0, 126.5+80, image=text_box_bg)  # background
address_entry = tk.Entry(
    bd=0, bg="#F6F7F9", highlightthickness=0)
address_entry.place(x=20.0, y=112+81, width=321.0, height=35)
canvas.create_text(
    20.0, 106+80, text="Address: ", fill="#515486",
    font=("Arial-BoldMT", int(13.0)), anchor="w")

cmnd_entry_img = canvas.create_image(
    180.0, 126.5+80*2, image=text_box_bg)  # background
cmnd_entry = tk.Entry(
    bd=0, bg="#F6F7F9", highlightthickness=0)
cmnd_entry.place(x=20.0, y=112+81*2, width=321.0, height=35)
canvas.create_text(
    20.0, 106+80*2, text="CMND: ", fill="#515486",
    font=("Arial-BoldMT", int(13.0)), anchor="w")

salary_entry_img = canvas.create_image(
    180.0+370, 126.5+80, image=text_box_bg)  # background
salary_entry = tk.Entry(
    bd=0, bg="#F6F7F9", highlightthickness=0)
salary_entry.place(x=20.0+370, y=112+81, width=321.0, height=35)
canvas.create_text(
    20.0+370, 106+80, text="Salary: ", fill="#515486",
    font=("Arial-BoldMT", int(13.0)), anchor="w")

phone_entry_img = canvas.create_image(
    180.0+370, 126.5+80*2, image=text_box_bg)  # background
phone_entry = tk.Entry(
    bd=0, bg="#F6F7F9", highlightthickness=0)
phone_entry.place(x=20.0+370, y=112+81*2, width=321.0, height=35)
canvas.create_text(
    20.0+370, 106+80*2, text="Phone: ", fill="#515486",
    font=("Arial-BoldMT", int(13.0)), anchor="w")

mail_entry_img = canvas.create_image(
    180.0, 126.5+80*3, image=text_box_bg)  # background
mail_entry = tk.Entry(
    bd=0, bg="#F6F7F9", highlightthickness=0)
mail_entry.place(x=20.0, y=112+81*3, width=321.0, height=35)
canvas.create_text(
    20.0, 106+80*3, text="Mail: ", fill="#515486",
    font=("Arial-BoldMT", int(13.0)), anchor="w")

R1 = Radiobutton(window, text="Staff", value=1,
                 bg="#F6F7F9", font=("Arial-BoldMT", int(12.0)))
R1.pack(anchor=W)
R1.place(x=20.0+370, y=106+80*3)

R2 = Radiobutton(window, text="Manager", value=2,
                 bg="#F6F7F9", font=("Arial-BoldMT", int(12.0)))
R2.pack(anchor=W)
R2.place(x=20.0+450, y=106+80*3)

R3 = Radiobutton(window, text="Guard", value=3,
                 bg="#F6F7F9", font=("Arial-BoldMT", int(12.0)))
R3.pack(anchor=W)
R3.place(x=20.0+550, y=106+80*3)

save_btn_img = tk.PhotoImage(file=ASSETS_PATH / "btn_save.png")
save_btn = tk.Button(
    image=save_btn_img, borderwidth=10, highlightthickness=0, relief="flat")
save_btn.place(x=140, y=440, width=195, height=69)

cancel_btn_img = tk.PhotoImage(file=ASSETS_PATH / "btn_cancel.png")
cancel_btn = tk.Button(
    image=cancel_btn_img, borderwidth=10, highlightthickness=0, relief="flat")
cancel_btn.place(x=350, y=440, width=195, height=69)

success_noti_btn_img = tk.PhotoImage(file=ASSETS_PATH / "noti_success.png")
success_noti_btn = tk.Button(
    image=success_noti_btn_img, borderwidth=10, highlightthickness=0, relief="flat")
success_noti_btn.place(x=240, y=520, width=200, height=79)

failed_noti_btn_img = tk.PhotoImage(file=ASSETS_PATH / "noti_failed.png")
failed_noti_btn = tk.Button(
    image=failed_noti_btn_img, borderwidth=10, highlightthickness=0, relief="flat")
failed_noti_btn.place(x=240, y=600, width=200, height=79)


window.resizable(False, False)
window.mainloop()
