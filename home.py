import webbrowser
import re
import sys
import os
import tkinter as tk
from pathlib import Path
from tkinter import *
from PIL import Image, ImageTk
# .Variables
# Path to asset files for this GUI window
ASSETS_PATH = Path(__file__).resolve().parent / "assets"


window = tk.Tk()
logo = tk.PhotoImage(file=ASSETS_PATH / "iconbitmap.gif")
window.call('wm', 'iconphoto', window._w, logo)
window.title("Login")
window.geometry("862x449")
window.configure(bg="#3A7FF6")
canvas = tk.Canvas(
    window, bg="#3A7FF6", height=519, width=862,
    bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)
canvas.create_rectangle(431, 0, 431 + 431, 0 + 519, fill="#FCFCFC", outline="")
canvas.create_rectangle(40, 160, 40 + 60, 160 + 5, fill="#FCFCFC", outline="")


canvas.create_text(
    650.5, 68.0, text="Account Login",
    fill="#515486", font=("Arial-BoldMT", int(38.0)))

R1 = Radiobutton(window, text="Nhân viên", value=1,
                 bg="#F6F7F9", font=("Arial-BoldMT", int(12.0)))
R1.pack(anchor=W)
R1.place(x=500.0, y=110.0)

R2 = Radiobutton(window, text="Quản lí", value=2,
                 bg="#F6F7F9", font=("Arial-BoldMT", int(12.0)))
R2.pack(anchor=W)
R2.place(x=710.0, y=110.0)

text_box_bg = tk.PhotoImage(
    file=ASSETS_PATH / "TextBox_Bg.png")  # Textbox background

username_entry_img = canvas.create_image(650.5, 167.5, image=text_box_bg)
username_entry = tk.Entry(bd=0, bg="#F6F7F9", highlightthickness=0)
username_entry.place(x=490.0, y=137+25, width=321.0, height=35)
username_entry.focus()
canvas.create_text(
    490.0, 156.0, text="User name: ", fill="#515486",
    font=("Arial-BoldMT", int(13.0)), anchor="w")

password_entry_img = canvas.create_image(650.5, 248.5, image=text_box_bg)
password_entry = tk.Entry(bd=0, bg="#F6F7F9", highlightthickness=0, show="*")
password_entry.place(x=490.0, y=218+25, width=321.0, height=35)
canvas.create_text(
    490.0, 234.5, text="Password: ", fill="#515486",
    font=("Arial-BoldMT", int(13.0)), anchor="w")


title = tk.Label(
    text="Welcome to App Machine Learning", bg="#3A7FF6",
    fg="white", font=("Arial-BoldMT", int(20.0)))
title.place(x=27.0, y=120.0)


generate_btn_img = tk.PhotoImage(file=ASSETS_PATH / "btn_l.png")
generate_btn = tk.Button(
    image=generate_btn_img, borderwidth=10, highlightthickness=0, relief="flat")
generate_btn.place(x=557, y=300, width=195, height=83)


window.resizable(False, False)
window.mainloop()
